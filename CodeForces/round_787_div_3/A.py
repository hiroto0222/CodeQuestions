for _ in range(int(input())):
    # a -> dogfood
    # b -> catfood
    # c -> food
    # x dogs, y cats

    a, b, c, x, y = map(int, input().split())
    
    if a >= x and b >= y:
        print("YES")
    elif c >= max(0, (x - a)) + max(0, (y - b)):
        print("YES")
    else:
        print("NO")