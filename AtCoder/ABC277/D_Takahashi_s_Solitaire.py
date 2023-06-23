# 1. take card and place on table
# 2. X is card placed on table last. if there are cards between X and (X + 1) % M, pick 1 and place on table
# smallest possible sum in remaining hands
# sort
# ie:
# M = 7
# 3 0 2 5 5 3 0 6 3
# 0 0 | 2 3 3 3 | 5 5 6 0 0 |

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

dd = []
t = A[0]

for i in range(N - 1):
    if A[i + 1] - A[i] <= 1:
        t += A[i + 1]
    else:
        dd.append(t)
        t = A[i + 1]

dd.append(t)

if len(dd) > 1 and 0 == A[0] and (M - 1) == A[-1]:
    tmp = dd.pop(len(dd) - 1)
    dd.append(dd[0] + tmp)
    dd.pop(0)

print(sum(A) - max(dd))
