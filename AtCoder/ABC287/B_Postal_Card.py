N, M = map(int, input().split())
S = [input()[3:] for _ in range(N)]
seen = set()
for _ in range(M):
    seen.add(input())

res = 0
for s in S:
    if s in seen: res += 1
print(res)