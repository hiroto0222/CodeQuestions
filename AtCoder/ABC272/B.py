N, M = map(int, input().split())
arr = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    curr = list(map(int, input().split()))
    for a in curr[1:]:
        for b in curr[1:]:
            arr[a - 1][b - 1] = True

print("Yes" if all([all(x) for x in arr]) else "No")