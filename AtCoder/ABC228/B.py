N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [False] * (N + 1)

i = X
ans = 0
while not dp[i]:
    dp[i] = True
    i = A[i]
    ans += 1

print(ans)