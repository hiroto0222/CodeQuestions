for _ in range(int(input())):
    arr = list(map(int, input().split()))
    x, y, z = sorted(arr)

    if y == z:
        print("YES")
        if x == y:
            print(x, x, x)
        else:
            print(x, x, y)
    else: print("NO")
