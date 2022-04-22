H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

for j in range(W):
    row = []
    for i in range(H):
        row.append(A[i][j])
    print(*row)

