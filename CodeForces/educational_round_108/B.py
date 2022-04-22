t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if k == (n - 1) + (m - 1)*n or k == (m - 1) + (n - 1)*m:
        print('YES')
    else:
        print('NO')