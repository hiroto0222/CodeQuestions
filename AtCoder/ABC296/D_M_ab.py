"""
find X that satisfies both:
    1. X = a * b
    2. X >= M
"""
N, M = map(int, input().split())

if M <= N:
    print(M)
    exit()

ans = float('inf')
for a in range(1, N + 1):
    b = (M + a - 1) // a  # b = math.ceil(M / a)
    if a > b:
        break
    if b <= N:
        ans = min(ans, a * b)

print(ans if ans < float('inf') else -1)
