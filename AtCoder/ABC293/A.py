S = list(input())
for i in range(1, len(S), 2):
    S[i - 1], S[i] = S[i], S[i - 1]
print("".join(S))