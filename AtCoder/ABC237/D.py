from collections import deque

N = int(input())
S = input()

queue = deque([N])
for i in range(N - 1, -1, -1):
    if (S[i] == "L"):
        queue.append(i)
    else:
        queue.appendleft(i)

print(*list(queue))
