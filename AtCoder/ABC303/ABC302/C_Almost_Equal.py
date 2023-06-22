import itertools

N, M = map(int, input().split())
S = list(input() for _ in range(N))
perms = list(itertools.permutations(S))

for perm in perms:
    ok = True
    for i in range(N - 1):
        cnt = 0
        for j in range(M):
            if perm[i][j] != perm[i + 1][j]:
                cnt += 1
        if cnt != 1:
            ok = False
    if ok:
        print("Yes")
        exit()

print("No")
