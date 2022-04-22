t = int(input())
for _ in range(t):
    r, b, d = map(int, input().split())
    if d == 0 and r == b:
        print('YES')
    elif abs(r - b) <= d:
        print('YES')
    else:
        if (r + b) <= (min(r, b) + min(r, b) * (d + 1)):
            print('YES')
        else:
            print('NO')
