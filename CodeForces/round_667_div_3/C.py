for _ in range(int(input())):
    n, x, y = map(int, input().split())
    if n == 2:
        print(x, y)
    else:
        ans = [x, y]
        x, y = max(x, y), min(x, y)
        for i in range(51):
            if (n - 2 - i) == 1:
                if y - (x - y) > 0:
                    ans.append(y - (x - y))
                else:
                    ans.append(x + (x - y))
                break
            if (x - y) % (n - 2 - i):
                break