N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx = 1
a, b = [0] * len(A), [0] * len(B)
i, j = 0, 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        a[i] = idx
        i += 1
    else:
        b[j] = idx
        j += 1
    idx += 1

while i < len(A):
    a[i] = idx
    i += 1
    idx += 1
while j < len(B):
    b[j] = idx
    j += 1
    idx += 1

print(*a)
print(*b)
