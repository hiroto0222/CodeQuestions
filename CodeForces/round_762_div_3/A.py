for _ in range(int(input())):
    s = input()
    n = len(s)

    if len(s) % 2 == 1:
        print("NO")
    else:
        for i in range(n // 2):
            if s[i] != s[i + n // 2]:
                print("NO")
                break
        else:
            print("YES")