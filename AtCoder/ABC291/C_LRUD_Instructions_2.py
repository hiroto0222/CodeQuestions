"""
5
RLURU
(0, 0) -> (1, 0) -> (0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
"""

N = int(input())
S = input()
visited = set([(0, 0)])

i, j = 0, 0
for c in S:
    if c == "R":
        i += 1
    elif c == "L":
        i -= 1
    elif c == "U":
        j += 1
    else:
        j -= 1
    
    if (i, j) in visited:
        print("Yes")
        exit()
    visited.add((i, j))

print("No")