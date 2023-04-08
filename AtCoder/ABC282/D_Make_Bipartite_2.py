"""
graph G can have multiple graphs

determine bipartite graph
1. 0 -> 1 -> 0 -> 1
2. when an odd length cycle exists -> always non bipartite

Cases:
1. if u - v are from different graphs, and both are bipartite, then G connecting u - v is still bipartite
2. if u - v are from the same graph, u and v must be different colors

Solution:
1. for each subgraph, make bipartite by keep tracking of counts of (black, white)
2. u - v is bad if from same subgraph and same color -> X
3. from total nC2 - M - X = number of u - v that is good
"""

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

colors = [-1] * N
res = N * (N - 1) // 2 - M
for u in range(N):
    if colors[u] != -1:
        continue

    color_cnts = [0, 0]
    colors[u] = 0
    stack = [u]
    while stack:
        v = stack.pop()
        if colors[v] == 0:
            color_cnts[0] += 1
        else:
            color_cnts[1] += 1

        for nv in graph[v]:
            if colors[nv] == -1:
                colors[nv] = colors[v] ^ 1
                stack.append(nv)
            elif colors[nv] != colors[v] ^ 1:
                exit(print(0))

    for cnt in color_cnts:
        res -= cnt * (cnt - 1) // 2

print(res)
