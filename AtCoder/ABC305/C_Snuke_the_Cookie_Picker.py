"""
5 6
......
..#.#.
..###.
..###.
......
-> (2, 4)
"""

H, W = map(int, input().split())
S = [input() for _ in range(H)]

for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue

        cnt = 0
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if r + dy < H and r + dy >= 0 and c + dx < W and c + dx >= 0:
                if S[r + dy][c + dx] == "#":
                    cnt += 1

        if cnt > 1:
            print(r + 1, c + 1)
            break
