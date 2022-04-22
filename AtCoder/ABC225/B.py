N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = "No"
for i in range(1, N + 1):
    if len(G[i]) == N - 1:
        ans = "Yes"
        break

print(ans)