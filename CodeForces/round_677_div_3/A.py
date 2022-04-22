for _ in range(int(input())):
    x = int(input())
    ans = 0
    for i in range(1, 10):
        curr_cnt = 0
        curr = 0
        for j in range(0, 4):
            curr += i*10**j
            curr_cnt += (j + 1)
            if curr == x:
                break

        ans += curr_cnt
        if curr == x:
            break
    
    print(ans)
