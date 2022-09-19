from math import floor


for _ in range(int(input())):
    # pairs of (a,b) such that lcm(a,b)/gcd(a,b) <= 3
    # lcm(a,b) = a*b / gcm(a,b)
    # l / g = a*b / g^2 = a/g * b/g <= 3
    # combinations (a,b) -> (a, b=a), (a, b=2a), (a, b=3a), (a=2b, b), (a=3b, b)
    #                    -> n, floor(n/2), floor(n/3), floor(n/2), floor(n/3)
    # sum up all combinations

    n = int(input())
    print(n + 2*(floor(n / 2) + floor(n / 3)))
