"""
if H[i + 1] > H[i] -> move to i + 1
"""

N = int(input())
H = list(map(int, input().split()))

curr = H[0]
for i in range(N - 1):
    if (H[i + 1] > H[i]):
        curr = H[i + 1]
    else:
        break

print(curr)