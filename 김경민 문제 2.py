#==================================================================
# 0/1 배낭 문제 DP 구현 

def knapSack_dp(W, wt, val, n):
    A = []
    for i in range(n + 1):
        row = []
        for w in range(W + 1):
            row.append(0)
        A.append(row)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w < wt[i-1]:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][W], A



n = 5
wt = [3, 1, 2, 2, 1]
val = [12, 10, 6, 7, 4]
W = 5

max_value, A = knapSack_dp(W, wt, val, n)

print("1. 최대 만족도 =", max_value)
print()
print("2. DP table")
for i in range(n + 1):
    for w in range(W + 1):
        print(A[i][w], end="   ")
    print()

print()
print("3. 선택된 물건 역추적")

items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]

selected = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i-1][w]:
        name, wt_i, val_i = items[i-1]
        selected.append(name)
        w -= wt_i

selected.reverse()
print("선택된 물건:", selected)
