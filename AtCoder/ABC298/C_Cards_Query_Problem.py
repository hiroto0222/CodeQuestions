"""
upto 2*10**5 boxes, cards

1 i j -> choose 1 card and write i, and place in box j
2 i   -> list all cards in box i in ascending order
3 i   -> list all boxes with card i in ascending order

dp[N][N]
dp[i][j] = # of cards for box i, card j
"""
from collections import defaultdict

N = int(input())
Q = int(input())
boxes = defaultdict(list)
cards = defaultdict(set)

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        card, box = query[1], query[2]
        boxes[box].append(card)
        cards[card].add(box)

    elif query[0] == 2:
        box = query[1]
        print(*sorted(boxes[box]))

    else:
        card = query[1]
        print(*sorted(list(cards[card])))
