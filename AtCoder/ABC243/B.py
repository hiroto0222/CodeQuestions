N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

seenA = set()
seenB = set()
x, y = 0, 0
for i in range(N):
    if A[i] == B[i]:
        x += 1
        continue
    if A[i] in seenB:
        y += 1
    if B[i] in seenA:
        y += 1
    seenA.add(A[i])
    seenB.add(B[i])

print(x)
print(y)