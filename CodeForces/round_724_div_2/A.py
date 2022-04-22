for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 'YES'
    flag = False
    curr_max = a[0]
    for val in a:
        if val > curr_max:
            curr_max = val
        if val < 0:
            flag = True
            break
    
    if not flag:
        print('YES')
        print(curr_max + 1)
        print(*range(curr_max + 1))
    else:
        print('NO')
    
    if flag:
