N, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

cheese.sort(key=lambda x: x[0], reverse=True)
ans, cnt = 0, 0
for i in range(N):
    curr_cnt = min(cheese[i][1], W - cnt)
    ans += cheese[i][0] * curr_cnt
    if (cnt + curr_cnt == W):
        break
    cnt += curr_cnt

print(ans)