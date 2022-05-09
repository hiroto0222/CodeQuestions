from collections import defaultdict

INF = (1 << 62) - 1


def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    L_max = defaultdict(lambda: -INF)
    R_min = defaultdict(lambda: INF)

    for s, (x, y) in zip(S, XY):
        if s == "L":
            L_max[y] = max(L_max[y], x)
        else:
            R_min[y] = min(R_min[y], x)

    for y in L_max.keys():
        if R_min[y] < L_max[y]:
            return True
    return False


print("Yes" if solve() else "No")