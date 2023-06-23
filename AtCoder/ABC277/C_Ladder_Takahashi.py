# ladder[i] -> A[i] to B[i] or B[i] to A[i]
# BFS to find max end point

from collections import defaultdict, deque

N = int(input())
ladders = defaultdict(list)
for _ in range(N):
    s, e = map(int, input().split())
    ladders[s].append(e)
    ladders[e].append(s)

stack = deque()
stack.append(1)
visited = set([1])
while stack:
    curr = stack.popleft()
    for v in ladders[curr]:
        if v not in visited:
            stack.append(v)
            visited.add(v)

print(max(visited))
