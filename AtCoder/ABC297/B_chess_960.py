"""
K, Q x 1
R, B, N x 2

conditions
1. S[x] and S[y] are B, then x % 2 != y % 2
2. K is between 2 R
"""

S = input()

B_pos = []
R_pos = []
K_pos = 0
for i, c in enumerate(S):
    if c == "B":
        B_pos.append(i)
    if c == "R":
        R_pos.append(i)
    if c == "K":
        K_pos = i

if B_pos[0] % 2 == B_pos[1] % 2:
    print("No")
    exit()
if K_pos < R_pos[0] or K_pos > R_pos[1]:
    print("No")
    exit()

print("Yes")
