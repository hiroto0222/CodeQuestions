"""
level l-dango
1. L + 1 string made from o, -
2. either 0 or L is -, rest is o

find largest l-dango, else -1
"""

N = int(input())
S = input()

res = -1
curr = 0
for c in S:
    if c == "-":
        res = max(res, curr)
        curr = 0
    else:
        curr += 1

if res < 0:
    print(-1)
    exit()

res = max(res, curr)
print(res if res > 0 else -1)
