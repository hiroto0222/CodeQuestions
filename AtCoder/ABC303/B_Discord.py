# N people in M photos
# in each photo, stand in single line
# in photo i, jth person from left is a[i][j]
# find people who never stood next to each other in any photo

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

pairs = list(list(False for _ in range(N)) for _ in range(N))
for i in range(M):
    for j in range(N - 1):
        p1, p2 = a[i][j], a[i][j + 1]
        pairs[p1 - 1][p2 - 1] = True

res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if not pairs[i][j] and not pairs[j][i]:
            res += 1

print(res)
