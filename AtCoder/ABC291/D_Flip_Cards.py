"""
3
1 2
4 2
3 4

use dp to keep track of flips
when at card i:
dp[i][0] = number of combinations when not flipping
dp[i][1] = number of combinations when flipping
only prev card matters
i = 0, dp = [[1, 1], [], []]
i = 1, dp = [[1, 1], [2, 1], []]
i = 2, dp = [[1, 1], [2, 1], [3, 1]]
res = dp[N][0] + dp[N][1] = 4

1. if curr[0] != prev[0] -> dp[i][0] += dp[i - 1][0]
2. if curr[0] != prev[1] -> dp[i][0] += dp[i - 1][1]
3. if curr[1] != prev[1] -> dp[i][1] += dp[i - 1][1]
4. if curr[1] != prev[0] -> dp[i][1] += dp[i - 1][0]
"""

MOD = 998244353
N = int(input())
dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]
prev = list(map(int, input().split()))

for i in range(1, N):
    curr = list(map(int, input().split()))

    if curr[0] != prev[0]:
        dp[i][0] += dp[i - 1][0]
    if curr[0] != prev[1]:
        dp[i][0] += dp[i - 1][1]
    if curr[1] != prev[1]:
        dp[i][1] += dp[i - 1][1]
    if curr[1] != prev[0]:
        dp[i][1] += dp[i - 1][0]

    if dp[i][0] >= MOD: dp[i][0] %= MOD
    if dp[i][1] >= MOD: dp[i][1] %= MOD
    
    prev = curr

res = (dp[N - 1][0] + dp[N - 1][1]) % MOD
print(res)