# f(x) = math.floor(x / a) + x % a

import math

def f(x, a):
    return math.floor(x / a) + x % a

for _ in range(int(input())):
    l, r, a = map(int, input().split())
    ans = r // a + r % a
    m = r // a * a - 1
    if m >= l:
        ans = max(ans, m // a + m % a)
    print(ans)