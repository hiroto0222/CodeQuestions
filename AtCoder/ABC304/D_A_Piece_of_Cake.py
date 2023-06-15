# N strawberries
# a -> cut vertically at x
# b -> cut horizontally at y
# such x, y never hit strawberries
# total pieces = (A + 1) * (B + 1)
# N -> 2 * 10**5
# A, B -> 2 * 10**5

# consider each strawberry
# check which piece the strawberry belongs to
# for A cut -> binary search to see where x
# for B cut -> binary search to see where y
# map[(x, y)]++

from bisect import bisect_left
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))


def P(x, y):
    x1 = bisect_left(a, x)
    y1 = bisect_left(b, y)
    return (x1, y1)


dic = defaultdict(int)
for x, y in coords:
    piece = P(x, y)
    dic[piece] += 1

vals = dic.values()
M = max(vals)
m = 0 if len(vals) < (A + 1) * (B + 1) else min(vals)

print(m, M)
