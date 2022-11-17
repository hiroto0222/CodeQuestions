for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    ans = [f[0] - s[0]]
    prev = f[0]

    for i in range(1, n):
        if s[i] <= prev:
            ans.append(f[i] - prev)
        else:
            ans.append(f[i] - s[i])
        prev = f[i]
    
    print(*ans)