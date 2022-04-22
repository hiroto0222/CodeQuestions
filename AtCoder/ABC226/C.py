"""
use graph to store possible routes to N
BFS Search from N
"""

N = int(input())
T = [0] * (N + 1)
G = [[] for _ in range(N + 1)]

for u in range(1, N + 1):
    T[u], k, *A = map(int, input().split())
    for v in A:
        G[u].append(v)
        
seen = [False] * (N + 1)
stack = [N]
seen[N] = True
ans = 0

while stack:
    curr_u = stack.pop()
    ans += T[curr_u]

    for v in G[curr_u]:
        if not seen[v]:
            seen[v] = True
            stack.append(v)

print(ans)