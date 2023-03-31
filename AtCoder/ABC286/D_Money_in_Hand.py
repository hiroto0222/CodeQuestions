"""
has B[i] number of A[i] yen
can reach X yen?

dp[i][j] = using upto ith coin, can we reach j yen?
dp[0 ~ M][0 ~ X]
when considering coin[i], if coin[i - 1][j - coin[i]] is true, then coin[i][j] is true
"""

N, X = map(int, input().split())
coins = []
for _ in range(N):
    A, B = map(int, input().split())
    coins.extend([A] * B)
M = len(coins)
dp = [[False for _ in range(X + 1)] for _ in range(M + 1)]
dp[0][0] = True

for i in range(1, M + 1):
    for j in range(X + 1):
        curr_coin = coins[i - 1]

        if dp[i - 1][j]:
            dp[i][j] = True
        
        if j - curr_coin >= 0 and dp[i - 1][j - curr_coin]:
            dp[i][j] = True

print("Yes" if dp[M][X] else "No")