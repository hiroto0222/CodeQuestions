for _ in range(int(input())):
    """
    n = 3, [1, 2, 3]
    [1, 2] [2, 3] [1, 3]

    n = 4, [4, 2, 1, 3]
    [4, 2, 1] [4, 2, 3] [2, 1, 3] [4, 1, 3]

    all sequences but 1 start with init
    find the 1 sequence
    """

    n = int(input())
    p = []
    seen_once, seen_more = {}, {}  # first_val: idx
    for i in range(n):
        curr = list(map(int, input().split()))
        p.append(curr)
        if curr[0] not in seen_once:
            seen_once[curr[0]] = i
        else:
            seen_more[curr[0]] = i
    
    first, rest = [], []
    for val in seen_once:
        if val in seen_more:
            first = val
        else:
            rest = p[seen_once[val]]
    
    print(*([first] + rest))
