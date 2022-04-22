from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnts = Counter(A)
for key in cnts.keys():
    if cnts[key] == 3:
        print(key)
        break
