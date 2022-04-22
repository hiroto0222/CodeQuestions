"""
グラフの同型判定

test all possible Vertexes and check against a
-> check if a[i][j] == b[permutation[i]][permutation[j]]
"""
from itertools import permutations
from math import perm

N, M = map(int, input().split())
a = [[False] * N for _ in range(N)]
b = [[False] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u][v] = a[v][u] = True

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    b[u][v] = b[v][u] = True

ans = False
for permutation in permutations(range(N)):
    ok = True
    for i in range(N):
        for j in range(N):
            if a[i][j] != b[permutation[i]][permutation[j]]:
                ok = False
    
    if ok:
        ans = True
    
print("Yes" if ans else "No")