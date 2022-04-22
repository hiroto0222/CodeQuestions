for _ in range(int(input())):
    s = list(map(int, input().split()))
    a = sorted(s)[2:]
    if max(s[:2]) in a and max(s[2:]) in a:
        print('YES')
    else:
        print('NO')