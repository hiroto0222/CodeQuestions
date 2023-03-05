from collections import defaultdict

N, Q = map(int, input().split())
players = defaultdict(int)

for _ in range(Q):
    c, x = map(int, input().split())

    if c == 3:
        if x in players and players[x] >= 2:
            print("Yes")
        else:
            print("No")
    else:
        players[x] += c
