"""
Q = T, A, B
T = 1 -> A follows B
T = 2 -> A unfollows B
T = 3 -> Yes if (A follows B and B follows A) else No

users[A] = set(following)
"""

from collections import defaultdict

N, Q = map(int, input().split())
users = defaultdict(set)

for _ in range(Q):
    T, A, B = map(int, input().split())

    if T == 1:
        users[A].add(B)
    elif T == 2:
        users[A].discard(B)
    else:
        if B in users[A] and A in users[B]:
            print("Yes")
        else:
            print("No")