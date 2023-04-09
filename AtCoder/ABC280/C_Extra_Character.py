"""
atcoder
atcorder

1. when S[i] != T[i] -> i is inserted letter
2. if all equal for i = [0, len(S)] then i = len(S) + 1 is inserted letter
"""

S = input()
T = input()

for i in range(len(S)):
    if S[i] != T[i]:
        print(i + 1)
        exit()

print(len(T))
