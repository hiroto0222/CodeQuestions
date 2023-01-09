for _ in range(int(input())):
    k = int(input())

    i = 0
    while k > 0:
        i += 1
        if (i % 3 == 0 or i % 10 == 3):
            continue
        k -= 1
    
    print(i)