"""
start at 0
N jumps -> i jump = a[i] or b[i]
can he reach X with N jumps

dp approach
dp[i][j] = 1 if can reach coord j with ith jumps
dp[i][j] = 0 if cannot reach coord j with ith jumps
"""

N, X = map(int, input().split())
a, b = [], []
for _ in range(N):
    curr_a, curr_b = map(int, input().split())
    a.append(curr_a)
    b.append(curr_b)

dp = [[0]*(X + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(X):
        if (dp[i][j] == 1):
            if (j + a[i] <= X):
                dp[i + 1][j + a[i]] = 1
            if (j + b[i] <= X):
                dp[i + 1][j + b[i]] = 1

print("Yes" if dp[-1][-1] == 1 else "No")