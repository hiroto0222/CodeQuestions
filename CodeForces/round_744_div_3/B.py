for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)

    if a == a_sorted:
        print(0)
        continue

    res = []
    for i in range(n):
        curr = a_sorted[i]
        idx = a.index(curr)
        l = idx + 1
        
        if l != n:
            res.append([l, n, 1])
        del a[idx]
        a.append(curr)
    
    print(len(res))
    for r in res:
        print(*r)
