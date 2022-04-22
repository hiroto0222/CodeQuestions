H, W, K = map(int, input().split())
arr = []
for _ in range(H):
    arr.append(list(input()))

ans = 0
for h_combo in range(2**H):
    for w_combo in range(2**W):
        curr_cnt = 0

        for i in range(H):
            for j in range(W):
                if (h_combo >> i) & 1 == 0 and (w_combo >> j) & 1 == 0:
                    if arr[i][j] == '#':
                        curr_cnt += 1
        
        if curr_cnt == K:
            ans += 1

print(ans)
