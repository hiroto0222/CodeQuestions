from math import gcd

N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(N):
        if i == j: continue
        xi, yi = coords[i]
        xj, yj = coords[j]
        xd, yd = xi - xj, yi - yj
        curr_gcd = gcd(xd, yd)
        ans.add((xd // curr_gcd, yd // curr_gcd))

print(len(ans))