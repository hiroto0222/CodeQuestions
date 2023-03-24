"""
1 x -> all elements of A with x
2 i x -> add x to A[i]
3 i -> print A[i]

adding to all elements -> save in var
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
replaced = None
changes = defaultdict(int)

for _ in range(Q):
    curr = list(map(int, input().split()))

    if curr[0] == 1:
        replaced = curr[1]
        changes = defaultdict(int)
    
    elif curr[0] == 2:
        changes[curr[1] - 1] += curr[2]
    
    else:
        if replaced == None:
            print(A[curr[1] - 1] + changes[curr[1] - 1])
        else:
            print(replaced + changes[curr[1] - 1])