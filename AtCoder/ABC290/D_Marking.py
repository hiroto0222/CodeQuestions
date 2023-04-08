"""
1. Mark square 0
2. repeat following (N - 1) times
    i. init a var x with (A + D) % N, where A is the index of the square marked last time
    ii. while square x is marked, repeat replacing x with (x + 1) % N
    iii. mark square x

ex:
N=4, D=2, K=3

mark square i=0

1.
x = (0 + 2) % 4 = 2 (not marked)
mark square i=2

2.
x = (2 + 2) % 4 = 0 (marked)
x = (0 + 1) % N = 1 (not marked)
mark square i=1

3.
x = (1 + 2) % 4 = 3 (not marked)
mark sqaure i=3
"""
import math

for _ in range(int(input())):
    N, D, K = map(int, input().split())
    period = N // math.gcd(N, D)
    count = (K - 1) // period
    print((D * (K - 1) + count) % N)
