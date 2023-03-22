"""
1 -> not yet called, not yet visited, smallest id is called
2, x -> already called, not yet visited, id x visits
3 -> already called, not yet visited, smallest id is called

find id when 3 happens

N = 4
1 -> {1}
1 -> {1, 2}
3 -> 1, {1, 2}
2 1 -> {2}
1 -> {2, 3}
2 3 -> {2}
3 -> 2, {2}
1 -> {2, 4}
2, 2 -> {4}
3 -> 4, {4}

heap
"""
from heapq import heappush, heappop

N, Q = map(int, input().split())
i = 1
heap = []
visited = set()
for _ in range(Q):
    curr = list(map(int, input().split()))
    
    if curr[0] == 1:
        heappush(heap, i)
        i += 1
    elif curr[0] == 2:
        visited.add(curr[1])
    else:
        while heap and heap[0] in visited:
            heappop(heap)
        print(heap[0])