for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = max(a)
    i = 0
    ans = -1
    flag = False
    while i < n and not flag:
        if a[i] == maxx:
            if i == 0:
                if maxx > a[i + 1]:
                    ans = i + 1
                    flag = True
            elif i == n - 1:
                if maxx > a[i - 1]:
                    ans = i + 1
                    flag = True
            else:
                if maxx > a[i + 1] or maxx > a[i - 1]:
                    ans = i + 1
                    flag = True
        i += 1
    print(ans)
