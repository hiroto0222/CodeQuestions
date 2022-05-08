from collections import deque

Q = int(input())
q = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        q.append((query[1], query[2]))
        continue
    
    tot = 0
    while query[1] > 0:
        curr_val, curr_cnt = q.popleft()
        if curr_cnt > query[1]:
            q.appendleft((curr_val, curr_cnt - query[1]))
            tot += curr_val * (query[1])
            break
        else:
            tot += curr_val * curr_cnt
            query[1] -= curr_cnt
    print(tot)