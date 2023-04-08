N, K = map(int, input().split())
S = list(input())

for i in range(N):
    if S[i] == "x":
        continue

    if K > 0:
        K -= 1
        continue

    S[i] = "x"

print("".join(S))
