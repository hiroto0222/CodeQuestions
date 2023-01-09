for _ in range(int(input())):
    a, b, c = map(int, input().split())

    n = 2 * abs(a - b)

    if a >= 1 and a <= n and b >= 1 and b <= n and c >= 1 and c <= n:
        x1 = c + n // 2
        x2 = c - n // 2
        print(x1 if x1 <= n else x2)
    else:
        print(-1)