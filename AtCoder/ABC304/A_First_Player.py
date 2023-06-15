N = int(input())
S = []
start = (10**9 + 1, 0)
for i in range(N):
    s, a = input().split()
    a = int(a)
    if a < start[0]:
        start = (a, i)
    S.append(s)

for i in range(N):
    print(S[(start[1] + i) % N])
