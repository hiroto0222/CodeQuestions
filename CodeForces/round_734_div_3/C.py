# k colors
# wonderful if:
# - each element is painted in one of k colors or not
# - no 2 equal values painted in same color
# - all k colors have same number of elements
# - max among all 3 conditions

from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    size = 0
    group = defaultdict(list)
    for i, val in enumerate(a):
        if len(group[val]) < k:
            group[val].append(i)
            size += 1
    
    size -= size % k
    groups = group.values()
    res = [0] * n
    color = 0
    for group in groups:
        for i in group:
            res[i] = color + 1
            color = (color + 1) % k
            size -= 1
            if size <= 0:
                break
    
    print(*res)