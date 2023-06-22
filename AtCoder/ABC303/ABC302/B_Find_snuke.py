H, W = map(int, input().split())
S = [input() for _ in range(H)]
word = "snuke"

# vertical
for i in range(H - 4):
    for j in range(W):
        curr = ""
        for di in range(5):
            curr += S[i + di][j]

        if curr == word:
            for di in range(5):
                print(i + di + 1, j + 1)
            exit()
        if curr == word[::-1]:
            for di in range(4, -1, -1):
                print(i + di + 1, j + 1)
            exit()

# horizontal
for j in range(W - 4):
    for i in range(H):
        curr = ""
        for dj in range(5):
            curr += S[i][j + dj]

        if curr == word:
            for dj in range(5):
                print(i + 1, j + dj + 1)
            exit()
        if curr == word[::-1]:
            for dj in range(4, -1, -1):
                print(i + 1, j + dj + 1)
            exit()

# diag
for i in range(H - 4):
    for j in range(W - 4):
        curr = ""
        for dd in range(5):
            curr += S[i + dd][j + dd]

        if curr == word:
            for dd in range(5):
                print(i + dd + 1, j + dd + 1)
            exit()
        if curr == word[::-1]:
            for dd in range(4, -1, -1):
                print(i + dd + 1, j + dd + 1)
            exit()
