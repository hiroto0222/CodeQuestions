N, M, C = map(int, input().split())
B = list(map(int, input().split()))

ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    temp = C
    for i in range(M):
        temp += A[i]*B[i]
    if temp > 0:
        ans += 1

print(ans)