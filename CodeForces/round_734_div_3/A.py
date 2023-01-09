for _ in range(int(input())):
    n = int(input())

    rem = n % 3
    if rem == 0:
        print(n // 3, n // 3)
    elif rem == 1:
        print(n // 3 + 1, n // 3)
    else:
        print(n // 3, n // 3 + 1)