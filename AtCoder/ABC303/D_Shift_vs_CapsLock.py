# 3 keys -> a, shift, caps
# initially caps off
# 1. spend X to press a -> "a" or "A"
# 2. spend Y to press shift + a -> "A" or "a"
# 3. spend Z to press caps
# min time to type S
#
# possible moves
# 1. X
# 2. Y
# 3. Z + X
# 4. Z + Y
# consider all possible moves using dp
# f(i, c) -> min cost to type up to S[i] when caps is on or off

X, Y, Z = map(int, input().split())
S = input()
N = len(S)
dp = [[float("inf"), float("inf")] for _ in range(N + 1)]
dp[0][0] = 0

for i, c in enumerate(S):
    if c == "a":
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][0] + Z + Y, dp[i][1] + Y)
    else:
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][0] + Z + X, dp[i][1] + X)

print(min(dp[-1]))
