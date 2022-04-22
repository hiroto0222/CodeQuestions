for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0 
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
        else:
            break
    
    if cnt == n:
        if cnt % 2 == 0:
            ans = "Second"
        else:
            ans = "First"
    else:
        if cnt == 0:
            ans = "First"
        
        if cnt % 2 != 0:
            ans = "Second"
        else:
            ans = "First"

    print(ans)