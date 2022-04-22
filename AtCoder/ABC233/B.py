l, r = map(int, input().split())
S = list(input())
l -= 1
r -= 1

while (l < r):
    S[l], S[r] = S[r], S[l]
    l += 1
    r -= 1

print("".join(S))