"""
m = MEX(X)
every int 0 <= i < m is contained in X
m is not contained in X
"""

N, K = map(int, input().split())
A = list(set(map(int, input().split())))
A.sort()
res = 0

if A[0] != 0:
    print(res)
    exit()

res = 1
for i in range(1, len(A)):
    if res >= K:
        break

    if A[i - 1] + 1 == A[i]:
        res += 1
    else:
        break

print(res)
