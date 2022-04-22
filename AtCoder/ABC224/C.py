"""
300C3 -> 4 * 10**6
for each combination -> check int area for each 3 possible bases
"""
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for p1 in range(N):
    x1, y1 = coords[p1]
    for p2 in range(p1):
        x2, y2 = coords[p2]
        for p3 in range(p2):
            x3, y3 = coords[p3]
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                ans += 1

print(ans)