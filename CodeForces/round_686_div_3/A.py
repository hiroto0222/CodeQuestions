for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n, 0, -1):
        a.append(i)
    if n % 2 == 0:
        print(*a)
    else:
        a[n // 2], a[(n // 2) - 1] = a[(n // 2) - 1], a[n // 2]
        print(*a)