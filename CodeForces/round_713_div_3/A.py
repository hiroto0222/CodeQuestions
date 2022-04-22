from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnts = Counter(a)
    print(a.index(cnts.most_common()[-1][0]) + 1)
