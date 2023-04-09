"""
repeat until A = B
1. if A > B, replace A with A - B
2. if A < B, replace B with B - A
"""

A, B = map(int, input().split())

if A == B:
    exit(print(0))

res = 0
while A != B:
    if A > B:
        if A % B == 0:
            res += (A // B - 1)
            break
        curr = (A // B)
        A -= curr * B
        res += curr
    elif B > A:
        if B % A == 0:
            res += (B // A - 1)
            break
        curr = B // A
        B -= curr * A
        res += curr

print(res)
