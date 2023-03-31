"""
for graph to be a path graph
1. number of edges is N - 1
2. number of edges from node is max 2
3. no sub graphs, all connected -> check using bfs
"""

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if M != N - 1:
    print("No")
    exit()

for u in range(1, N + 1):
    if len(graph[u]) > 2:
        print("No")
        exit()

stack = [1]
visited = set()
while stack:
    for _ in range(len(stack)):
        u = stack.pop()
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                stack.append(v)

print("Yes" if len(visited) == N else "No")