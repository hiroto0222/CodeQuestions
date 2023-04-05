N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

dp = [False for _ in range(X + 1)]
dp[0] = True

for i in range(X):
    if dp[i]:
        for a in A:
            if i + a <= X and (i + a) not in B:
                dp[i + a] = True

print("Yes" if dp[X] else "No")
