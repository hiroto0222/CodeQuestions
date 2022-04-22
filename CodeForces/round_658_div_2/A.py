for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = "NO"
    if len(a) > len(b):
        a, b = set(b), a
    else:
        a, b = set(a), b
    
    for i in range(len(b)):
        if b[i] in a:
            ans = "YES"
            print(ans)
            print(1, b[i])
            break
    else:
        print(ans)
