"""
x = 1
1. x * a
2. flip start and end digits (12) -> (21)
create unweighted graph with vertex as numbers
shortest route -> BFS

max digits -> 10**6
"""

from collections import deque

a, N = map(int, input().split())
M = 1
while M <= N:
    M *= 10

dist = [-1]*M
dist[1] = 0
Q = deque()
Q.append(1)

while len(Q):
    curr = Q.popleft()
    curr_dist = dist[curr]

    op_1 = a * curr
    if op_1 < M and dist[op_1] == -1:
        dist[op_1] = curr_dist + 1
        Q.append(op_1)
    
    if curr >= 10 and curr % 10 != 0:
        s = str(curr)
        op_2 = int(s[-1] + s[:-1])
        if op_2 < M and dist[op_2] == -1:
            dist[op_2] = curr_dist + 1
            Q.append(op_2)

print(dist[N])
