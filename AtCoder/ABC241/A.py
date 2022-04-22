a = list(map(int, input().split()))

idx = 0
cnt = 0
while cnt < 2:
    idx = a[idx]
    cnt += 1

print(a[idx])