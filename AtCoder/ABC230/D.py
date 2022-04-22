N, D = map(int, input().split())
walls = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
end = 0
walls.sort(key=lambda x: x[1])

for l, r in walls:
    if end < l:
        cnt += 1
        end = r + D - 1

print(cnt)