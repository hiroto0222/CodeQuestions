grid = [input() for _ in range(8)]
col = "abcdefgh"
row = "87654321"
for i in range(8):
    for j in range(8):
        if grid[i][j] == "*":
            print(col[j] + row[i])