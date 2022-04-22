N, M = map(int, input().split())
hands = [list(input()) for _ in range(2*N)]
rank = [[0, i] for i in range(2*N)]

judge = {"G": {"C": 1, "P": 2}, "C": {"P": 1, "G": "2"}, "P": {"G": 1, "C": 2}}

for j in range(M):
    for i in range(N):
        p1 = rank[2 * i][1]
        p2 = rank[2 * i + 1][1]
        h1 = hands[p1][j]
        h2 = hands[p2][j]

        if h1 == h2:
            continue
        else:
            winner = judge[h1][h2]
            if winner == 1:
                rank[2 * i][0] -= 1
            else:
                rank[2 * i + 1][0] -= 1
        
        rank.sort()

for i in range(2*N):
    print(rank[i][1] + 1)