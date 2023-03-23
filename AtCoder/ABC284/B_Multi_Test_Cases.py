for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    res = 0
    for val in A:
        if val % 2 != 0:
            res += 1
    print(res)