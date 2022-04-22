N, K = map(int, input().split())
S = [0] * N

for i in range(N):
    S[i] = sum(map(int, input().split()))

T = sorted(S, reverse=True)[K - 1]
for x in S:
    print("Yes" if x + 300 >= T else "No")