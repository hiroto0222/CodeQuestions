N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

max_len = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        max_len = max(max_len, ((coords[j][0] - coords[i][0])**2 + (coords[j][1] - coords[i][1])**2)**0.5)

print(max_len)