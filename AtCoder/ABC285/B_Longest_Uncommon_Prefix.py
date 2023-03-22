"""
max l is n - i
i = 1 -> 
"""

N = int(input())
S = input()

for i in range(1, N):
    l = 0
    for j in range(N - i):
        if S[j] == S[j + i]:
            break
        else:
            l += 1
    print(l)