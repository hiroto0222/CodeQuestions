H, W = map(int, input().split())

for _ in range(H):
    curr = list(map(int, input().split()))
    res = []
    for val in curr:
        if val == 0:
            res.append(".")
        else:
            res.append(chr(ord("A") + val - 1))
    print("".join(res))