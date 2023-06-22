# start from (0, 0) with H health
# M health pots, item[i] at (xi, yi)
# for every move, spend H - 1 and move in S[i] dir
# if health < 0 -> dead
# if item exists and health < K, take item and health = K

N, M, H, K = map(int, input().split())
S = input()
items = set()
for _ in range(M):
    x, y = map(int, input().split())
    items.add((x, y))

curr = (0, 0)
for i in range(N):
    H -= 1
    if S[i] == "L":
        curr = (curr[0] - 1, curr[1])
    elif S[i] == "R":
        curr = (curr[0] + 1, curr[1])
    elif S[i] == "U":
        curr = (curr[0], curr[1] + 1)
    else:
        curr = (curr[0], curr[1] - 1)

    if H < 0:
        print("No")
        exit()

    if curr in items and H < K:
        H = K
        items.remove(curr)

print("Yes")
