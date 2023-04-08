N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in B:
    res += A[i - 1]
print(res)
