"""
days = A + B - 1
"""

from collections import Counter


N = int(input())
C = Counter()
for _ in range(N):
    a, b = map(int, input().split())
    C[a] += 1
    C[a + b] -= 1

ans = [0] * (N + 1)
days = sorted(C.keys())
prev_day = 0
cnt = 0

for curr_day in days:
    ans[cnt] += curr_day - prev_day
    cnt += C[curr_day]
    prev_day = curr_day

print(*ans[1:])