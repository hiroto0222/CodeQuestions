class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return

        if y > x:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


N, M = map(int, input().split())
if M == 0:
    print(*list(range(1, N + 1)))
    exit()

A = list(map(int, input().split()))

uf = UnionFind(N)
for a in A:
    uf.merge(a - 1, a)

res = []
visited = [False for _ in range(N)]

for i in range(N):
    if visited[i]: continue

    if uf.find(i) < 0:
        res.append(i + 1)
    else:
        x = uf.find(i)
        for j in range(x, i - 1, -1):
            res.append(j + 1)
            visited[j] = True

print(*res)
