from collections import Counter


N = int(input())
S = list(map(int, input().split()))
cnts = Counter(S)

ans = 0
for a in range(1, 1001):
    for b in range(1, 1001):
        curr = 4*a*b + 3*a + 3*b
        if curr in cnts:
            ans += cnts.pop(curr)
        
        if len(cnts) == 0:
            break

print(N - ans)