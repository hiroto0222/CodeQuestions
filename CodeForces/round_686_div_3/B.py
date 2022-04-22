from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnts = Counter(a)
    b = [k for k, v in cnts.items() if v == 1]
    if len(b) == 0:
        print(-1)
    else:
        print(a.index(min(b)) + 1)