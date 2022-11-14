# block[i] -> 1 x math.ceil(i / 2)
# if n is odd -> can make square with all blocks
# if n is even -> n // 2 side square


for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1:
        print(n // 2 + 1)
    else:
        print(n // 2)