for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    if n >= ((b - y) + (a - x)):
        print(x * y)
    else:
        k = max(a - n, x)
        l = max(b - n, y)
        print(min(k*(b - (k - (a - n))), l*(a - (l - (b - n)))))
    