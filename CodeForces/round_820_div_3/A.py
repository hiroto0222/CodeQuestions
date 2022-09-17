for _ in range(int(input())):
    # first elevator on floor a
    # second elevator on floor b and goes to floor c
    # t_1 = a - 1
    # t_2 = abs(c - b) + abs(c - b) - 1

    a, b, c = map(int, input().split())
    t_1 = a - 1
    t_2 = abs(c - b) + c - 1

    if t_1 == t_2:
        print(3)
    elif t_1 > t_2:
        print(2)
    else:
        print(1)