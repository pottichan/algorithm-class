import time

# 반복문으로 팩토리얼 계산
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀로 팩토리얼 계산
def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

# 실행 시간 측정 함수
def run_with_time(func, n: int):
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return result, elapsed

# 전역 테스트 데이터
TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# 메뉴 출력
def print_menu():
    print("\n==== Factorial Tester ====")
    print("1) 반복문으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("========================")

# 메인 루프
def main():
    while True:
        print_menu()
        choice = input("메뉴 선택: ")

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["1", "2", "3"]:
            try:
                n = int(input("n 값(정수, 0 이상)을 입력하세요: "))
            except ValueError:
                print("정수(0 이상의 숫자)만 입력하세요.")
                continue

            try:
                if choice == "1":
                    result, t = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result} (실행 시간: {t:.6f}초)")

                elif choice == "2":
                    result, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result} (실행 시간: {t:.6f}초)")

                elif choice == "3":
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    res_rec, t_rec = run_with_time(factorial_rec, n)

                    # 결과 출력
                    print(f"[반복] {n}! = {res_iter}")
                    print(f"[재귀] {n}! = {res_rec}")

                    # 일치 여부
                    print("결과 일치 여부: 일치" if res_iter == res_rec else "결과 일치 여부: 불일치")

                    # 실행 시간 비교
                    print(f"[반복] 시간: {t_iter:.6f} s | [재귀] 시간: {t_rec:.6f} s")

            except ValueError as e:
                print(e)
            except RecursionError:
                print("재귀 깊이를 초과했습니다. (RecursionError)")

        elif choice == "4":
            print("\n[테스트 데이터 실행]")
            for n in TEST_DATA:
                try:
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    res_rec, t_rec = run_with_time(factorial_rec, n)

                    # 결과 일치 여부
                    same = (res_iter == res_rec)

                    # 첫 줄: n, same 여부, 실행시간
                    print(f"n= {n} | same={same} | iter={t_iter:.6f}s, rec={t_rec:.6f}s")

                    # 둘째 줄: 결과값
                    print(f"{n}! = {res_iter}")

                except RecursionError:
                    print(f"n= {n} | RecursionError (재귀 깊이 초과)")

        else:
            print("올바른 메뉴 번호를 입력하세요.")

if __name__ == "__main__":
    main()
