N, M = map(int, input().split())
S = []
for _ in range(M):
    int(input())
    S.append(list(map(int, input().split())))

res = 0
for combo in range(2**M):
    check = [False for _ in range(N)]
    for i in range(M):
        if combo >> i & 1:
            for s in S[i]:
                check[s - 1] = True

    if all(check):
        res += 1

print(res)
