for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print('NO')
    else:
        print('YES')
        remains = []
        for i in range(1, n):
            if a[0] != a[i]:
                print(1, i + 1)
                x = i + 1
            else:
                remains.append(i + 1)
        for val in remains:
            print(x, val)
    