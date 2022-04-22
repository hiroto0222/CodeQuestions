from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if gcd(a[i], 2*a[j]) > 1 or gcd(2*a[i], a[j]) > 1:
                ans += 1
    print(ans)
    