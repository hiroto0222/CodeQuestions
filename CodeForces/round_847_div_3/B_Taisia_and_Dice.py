for _ in range(int(input())):
    """
    s = sum of all dice
    r = sum of n - 1

    n = 3
    s = 9
    r = 5
    m = 4
    [4, 4] [4]
    want to decrease by 12 - 9 = 3
    for each dice decrease 3 // (n - 1)
    for remaining subtract 3 % (n - 1)
    """

    n, s, r = map(int, input().split())
    m = s - r
    res = [m] * n
    t = sum(res) - s

    for i in range(n - 1):
        res[i] -= t // (n - 1)
    for i in range(t % (n - 1)):
        res[i] -= 1
    
    print(*res)
