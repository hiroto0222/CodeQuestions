for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        ans = abs(a - b) // 10
        if abs(a - b) % 10 != 0:
            print(ans + 1)
        else:
            print(ans)
