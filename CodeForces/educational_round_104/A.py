t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    prev = None
    for val in a:
        if prev == None:
            prev = val
        else:
            if prev == val:
                cnt += 1
                prev = val

    print(len(a) - cnt)