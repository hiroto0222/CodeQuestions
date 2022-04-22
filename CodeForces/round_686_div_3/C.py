from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print(0)
    else:
        b = []
        prev = None
        cnt = {}
        for val in a:
            if prev == None:
                b.append(val)
                cnt[val] = 2
            else:
                if prev != val:
                    b.append(val)
                    if val not in cnt:
                        cnt[val] = 2
                    else:
                        cnt[val] += 1
            prev = val

        cnt[b[0]] = max(1, (cnt[b[0]] - 1))
        cnt[b[-1]] = max(1, (cnt[b[-1]] - 1))
        
        print(min(cnt.values()))
