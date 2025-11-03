
from dataclasses import dataclass
from typing import Optional, Iterator, Tuple


# -----------------------------
# Node (단순 연결 리스트 노드)
# -----------------------------
class Node:
    """단순 연결 리스트를 위한 노드 클래스"""
    def __init__(self, elem, next: Optional["Node"] = None):
        self.data = elem
        self.link = next

    def append(self, new: Optional["Node"]) -> None:
        """현재 노드 다음에 new 노드를 삽입"""
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self) -> Optional["Node"]:
        """현재 노드의 다음 노드를 삭제한 후 반환"""
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


# -----------------------------
# Book (도서 데이터 클래스)
# -----------------------------
@dataclass
class Book:
    book_id: int
    title: str
    author: str
    year: int

    def __str__(self) -> str:
        return f"{self.book_id} | {self.title} | {self.author} | {self.year}"


# -----------------------------
# LinkedList (단순 연결 리스트)
# -----------------------------
class LinkedList:
    """Book 객체를 저장하는 단순 연결 리스트"""
    def __init__(self):
        self.head: Optional[Node] = None

    def isEmpty(self) -> bool:
        return self.head is None

    def __iter__(self) -> Iterator[Book]:
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.link

    def __len__(self) -> int:
        n = 0
        cur = self.head
        while cur:
            n += 1
            cur = cur.link
        return n

    # 과제 요구: 제목으로 도서 찾기
    def find_by_title(self, title: str) -> Optional[Book]:
        cur = self.head
        while cur:
            if cur.data.title == title:
                return cur.data
            cur = cur.link
        return None

    # 과제 요구: 제목으로 위치(pos, 이전노드 포함) 찾기
    def find_pos_by_title(self, title: str) -> Tuple[Optional[Node], Optional[Node]]:
        """return (prev, curr)"""
        prev = None
        curr = self.head
        while curr:
            if curr.data.title == title:
                return prev, curr
            prev, curr = curr, curr.link
        return None, None

    # 편의: book_id 중복 확인
    def exists_book_id(self, book_id: int) -> bool:
        for b in self:
            if b.book_id == book_id:
                return True
        return False

    # 삽입: 맨 뒤에 추가
    def append_book(self, book: Book) -> None:
        node = Node(book)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.link is not None:
            cur = cur.link
        cur.link = node

    # 삭제: 주어진 노드 삭제
    def remove_node(self, prev: Optional[Node], curr: Node) -> None:
        if prev is None:
            # head 삭제
            self.head = curr.link
        else:
            prev.link = curr.link


# -----------------------------
# BookManagement (메뉴 및 기능)
# -----------------------------
class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id: int, title: str, author: str, year: int) -> None:
        if self.books.exists_book_id(book_id):
            print("오류: 중복된 책 번호입니다.")
            return
        self.books.append_book(Book(book_id, title, author, year))
        print("도서 추가 완료.")

    def remove_book(self, title: str) -> None:
        prev, curr = self.books.find_pos_by_title(title)
        if curr is None:
            print("삭제 실패: 해당 제목의 도서가 없습니다.")
            return
        self.books.remove_node(prev, curr)
        print("도서 삭제 완료.")

    def search_book(self, title: str) -> None:
        book = self.books.find_by_title(title)
        if book is None:
            print("조회 실패: 해당 제목의 도서가 없습니다.")
        else:
            print(str(book))

    def display_books(self) -> None:
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        for b in self.books:
            print(str(b))

    def _menu(self) -> None:
        print("\n===== 도서 관리 프로그램 =====")
        print("1. 도서 추가")
        print("2. 도서 삭제 (책 제목)")
        print("3. 도서 조회 (책 제목)")
        print("4. 전체 도서 목록 출력")
        print("5. 프로그램 종료")

    def run(self) -> None:
        while True:
            self._menu()
            try:
                choice = int(input("메뉴 선택: ").strip())
            except ValueError:
                print("입력 오류: 숫자를 입력하세요.")
                continue

            if choice == 1:
                try:
                    book_id = int(input("책 번호: ").strip())
                    title = input("책 제목: ").strip()
                    author = input("저자: ").strip()
                    year = int(input("출판 연도: ").strip())
                except ValueError:
                    print("입력 오류: 번호와 연도는 정수로 입력하세요.")
                    continue
                self.add_book(book_id, title, author, year)

            elif choice == 2:
                title = input("삭제할 책 제목: ").strip()
                self.remove_book(title)

            elif choice == 3:
                title = input("조회할 책 제목: ").strip()
                self.search_book(title)

            elif choice == 4:
                self.display_books()

            elif choice == 5:
                print("프로그램을 종료합니다.")
                break
            else:
                print("입력 오류: 1~5 중에서 선택하세요.")


if __name__ == "__main__":
    app = BookManagement()
    app.run()
