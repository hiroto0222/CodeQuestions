N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
for i, j in zip(range(P - 1, Q), range(R - 1, S)):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

print(*A)