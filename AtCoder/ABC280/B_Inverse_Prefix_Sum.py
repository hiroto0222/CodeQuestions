N = int(input())
S = list(map(int, input().split()))

res = [0] * N
res[0] = S[0]
prev = S[0]

for i in range(1, N):
    res[i] = S[i] - prev
    prev += res[i]

print(*res)
