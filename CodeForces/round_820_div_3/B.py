for _ in range(int(input())):
    # ord("a") - 96 is pos of alphabet
    # backwards

    n = int(input())
    s = input()
    ans = ""

    i = n - 1
    while i >= 0:
        curr = int(s[i])

        if curr == 0:
            curr_char = chr(int(s[i - 2] + s[i - 1]) + 96)
            i -= 3
        else:
            curr_char = chr(curr + 96)
            i -= 1
        
        ans = curr_char + ans
    
    print(ans)