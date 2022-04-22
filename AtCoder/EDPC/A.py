N = int(input())
h = list(map(int, input().split()))

dp = [0]*N
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[i] = abs(h[1] - h[0])
    else:
        dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))

print(dp[N - 1])