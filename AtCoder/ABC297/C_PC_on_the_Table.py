"""
perform
if S[i][j] = S[i][j + 1] = "T" then replace S[i][j] = "P" and S[i][j + 1] = "C"

maximize number of operations
"""

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    j = 1
    while j < W:
        if S[i][j] == "T" and S[i][j - 1] == "T":
            S[i][j] = "C"
            S[i][j - 1] = "P"
            j += 2
        else: j += 1
    print("".join(S[i]))
