"""
want A[i] - A[j] = X

ex:
6 5
3 1 4 1 5 9

i = 0 (-2, 8)
i = 1 (-4, 6)
i = 2 (-1, 9)
i = 3 (-4, 6)
i = 4 (0, 10)
i = 5 9 exists

"""

N, X = map(int, input().split())
A = list(map(int, input().split()))
seen = set()

if X == 0:
    print("Yes")
    exit()

for val in A:
    if val in seen:
        print("Yes")
        exit()
    
    seen.add(val - X)
    seen.add(val + X)

print("No")