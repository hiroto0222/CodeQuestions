N, P = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for val in a:
    if val < P: cnt += 1

print(cnt)