for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min_pos = a.index(min(a))
    max_pos = a.index(max(a))
    min_pos, max_pos = min(min_pos, max_pos), max(min_pos, max_pos)
    l = max_pos + 1
    r = n - min_pos
    both = min_pos + 1 + (n - max_pos)
    print(min([l, r, both]))
