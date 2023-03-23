from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

res = 0
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if visited[i]: continue
    res += 1
    dfs(i)

print(res)