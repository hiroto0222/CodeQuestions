N = int(input())
A = list(map(int, input().split()))
called = [False] * N

for i in range(N):
    if not called[i]:
        called[A[i] - 1] = True

cnt = 0
ans = []
for i in range(N):
    if not called[i]:
        cnt += 1
        ans.append(i + 1)
print(cnt)
print(*ans)