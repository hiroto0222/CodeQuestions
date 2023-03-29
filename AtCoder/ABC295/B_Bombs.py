ROWS, COLS = map(int, input().split())
grid = [list(input()) for _ in range(ROWS)]
res = [[False for _ in range(COLS)] for _ in range(ROWS)]

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] in "123456789":
            for di in range(ROWS):
                for dj in range(COLS):
                    if abs(di - i) + abs(dj - j) <= int(grid[i][j]):
                        res[di][dj] = True

for i in range(ROWS):
    for j in range(COLS):
        if res[i][j]:
            grid[i][j] = "."

for row in grid:
    print("".join(row))