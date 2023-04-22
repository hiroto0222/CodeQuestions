"""
winner
1. for color T, largest R[i] wins
2. if no T, largest R[i] for C[i] wins
"""

N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

colors = {}  # store max of (R[i], i)
for i in range(N):
    if C[i] in colors:
        colors[C[i]] = max(colors[C[i]], (R[i], i), key=lambda x: x[0])
    else:
        colors[C[i]] = (R[i], i)

if T in colors:
    print(colors[T][1] + 1)
else:
    print(colors[C[0]][1] + 1)
