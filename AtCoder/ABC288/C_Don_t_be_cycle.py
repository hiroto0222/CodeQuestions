class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.rank = [1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parents[x] = y


N, M = map(int, input().split())
uf = UnionFind(N)
res = 0
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if uf.find(u) == uf.find(v):
        res += 1
    uf.union(u, v)

print(res)