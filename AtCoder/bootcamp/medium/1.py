N = int(input())
a = [int(input()) for _ in range(N)]

cnt = 0
curr_idx = 0
for _ in range(10**5):
    cnt += 1
    curr_idx = a[curr_idx] - 1

    if curr_idx == 1:
        print(cnt)
        break
else:
    print(-1)