"""
given (x[i], k[i])
get y such that A[y] = x[i] for kth time
DNE -> -1
"""

N, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

hashmap = {}
for i in range(N):
    if a[i] not in hashmap:
        hashmap[a[i]] = [i + 1]
    else:
        hashmap[a[i]].append(i + 1)

for i in range(Q):
    x, k = queries[i][0], queries[i][1]
    if x in hashmap and k <= len(hashmap[x]):
        print(hashmap[x][k - 1])
    else:
        print(-1)
