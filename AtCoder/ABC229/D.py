"""
sliding window approach
"""
from collections import deque

S = input()
K = int(input())

que = deque()
left = 0
ans = 0

for right, val in enumerate(S):
    if val == ".":
        que.append(right)
    
    while len(que) > K:
        i = que.popleft()
        left = i + 1
    
    ans = max(ans, right - left + 1)


print(ans)