from itertools import combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
combos = list(combinations(list(range(N)), 2))
res = 0

for x, y in combos:
    flag = True
    for i in range(M):
        if S[x][i] != "o" and S[y][i] != "o":
            flag = False
            break
    if flag:
        res += 1

print(res)
