H, W = map(int, input().split())
res = 0
for _ in range(H):
    S = input()
    for c in S:
        if c == "#":
            res += 1

print(res)
