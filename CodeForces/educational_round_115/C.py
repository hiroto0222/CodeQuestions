"""
a[i] -> i = 1,..,n
k -> mean of a
remove 2 elements from a so that k remains the same
get number of pairs of [i, j] i < j such that above holds

k = sum(a) / n
must hold that -> sum(*a) = (n - 2) * k
                  sum(a) - ele = nk - 2k
                  ele = 2k
must find pairs a[i] + a[j] = 2k
keep track of occurences for each element
"""

from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = 2 * (sum(a) / n)
    ans = 0

    if (x % 1 != 0):
        print(ans)
        continue
    
    x = int(x)
    hash = defaultdict(int)
    for val in a:
        hash[val] += 1
    
    for val in a:
        if (x - val) in hash:
            ans += hash[x - val]
        if (x - val) == val:
            ans -= 1
    
    print(ans // 2)