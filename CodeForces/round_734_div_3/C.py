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
    for i in range(len(a)):
        if len(group[a[i]]) < k:
            size += 1
            group[a[i]].append(i)

    res = [0] * n
    groups = group.values()
    size -= size % k

    col = 0
    for group in groups:
        for val in group:
            res[val] = col + 1
            col = (col + 1) % k
            size -= 1
            if size <= 0:
                break

    print(*res)