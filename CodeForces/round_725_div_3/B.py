for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if set(a) == 1:
        print(0)
    elif (sum(a) % n) != 0:
        print(-1)
    else:
        x = sum(a) // n
        cnt = 0
        for val in a:
            if val > x:
                cnt += 1
        print(cnt)