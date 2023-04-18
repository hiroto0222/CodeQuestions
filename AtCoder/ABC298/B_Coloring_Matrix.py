"""
rotate A
A[i][j] = A[N + 1 - j][i] for all i, j
3 times till back to original
"""

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

ones = [[i, j] for i in range(N) for j in range(N) if A[i][j] == 1]

if not len(ones):
    print("Yes")
    exit()

for _ in range(4):
    curr = True
    for idx in range(len(ones)):
        i, j = ones[idx]
        ones[idx] = [N - 1 - j, i]
        if B[i][j] != 1:
            curr = False

    if curr:
        print("Yes")
        exit()

print("No")
