for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, 0
    ans = 0
    for i in range(n):
        if a[i] == 1:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            r = i
            break
    for i in range(l, r + 1):
        if a[i] == 0:
            ans += 1
    
    print(ans)