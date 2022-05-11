N = int(input())
A = list(map(int, input().split()))

A = set(A)
for val in range(2001):
    if val not in A:
        print(val)
        break