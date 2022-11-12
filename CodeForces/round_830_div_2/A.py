# a[i] = gcd(a[i], i)
# cost n - i + 1
# gcd(n - 1, n) = 1
# want to choose i = n - 1 or i = n for cheapest operations
# i = n - 1 -> 2
# i = n -> 1

from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        if a[0] == 1: print(0)
        else: print(1)
        continue

    res = gcd(a[0], a[1])
    for i in range(2, n):
        res = gcd(res, a[i])
    
    if res == 1:
        print(0)
    elif gcd(res, gcd(a[n - 1], n)) == 1:
        print(1)
    elif gcd(res, gcd(a[n - 2], n - 1)) == 1:
        print(2)
    else:
        print(3)