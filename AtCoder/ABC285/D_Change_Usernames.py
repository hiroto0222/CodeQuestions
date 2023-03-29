"""
cannot if there is a cycle in the graph

ie:
a b
y z
c d
x y
b c

a -> b -> c -> d
x -> y -> z
"""
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
    
    def find(self, x):
        if self.parent[x] < 0:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        self.parent[x] = y

# class UnionFind:
#     def __init__(self,N):
#         self.N=N
#         self.parent_size=[-1]*N
#     def leader(self,a):
#         if self.parent_size[a]<0: return a
#         self.parent_size[a]=self.leader(self.parent_size[a])
#         return self.parent_size[a]
#     def merge(self,a,b):
#         x,y=self.leader(a),self.leader(b)
#         if x == y: return
#         if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
#         self.parent_size[x] += self.parent_size[y]
#         self.parent_size[y]=x
#     def same(self,a,b):
#         return self.leader(a) == self.leader(b)
    
N = int(input())
UF = UnionFind(2*N)
seen = {}

for i in range(N):
    S, T = input().split()
    if S not in seen:
        seen[S] = 2*i
    if T not in seen:
        seen[T] = 2*i + 1

    if UF.same(seen[S], seen[T]):
        print("No")
        exit()
    else:
        UF.merge(seen[S], seen[T])

print("Yes")