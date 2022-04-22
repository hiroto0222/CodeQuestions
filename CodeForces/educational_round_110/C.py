for _ in range(int(input())):
    s = input()
    n = len(s)
    left, right = 0, 1
    prev = None
    ans = 0
    while left < n and right < n:
        print('curr string: ', s[left:right + 1])
        if prev == None:
            if (s[left] + s[right]) in ['01', '10', '?0', '?1']:
                prev = s[right]
                right += 1
                ans += 1
            elif s[right] == '?':
                if s[left] == '0':
                    prev = '1'
                elif s[left] == '1':
                    prev = '0'
                else:
                    prev = '?'
                right += 1
                ans += 1
            else:
                if s[left] == '?' or s[right] == '?':
                    left = right - 1
                    prev = None
                else:
                    left = right
                    right += 1
        else:
            if (prev + s[right]) in ['01', '10', '?0', '?1']:
                prev = s[right]
                ans += (right - left) 
                right += 1
            elif s[right] == '?':
                if s[left] == '0':
                    prev = '1'
                elif s[left] == '1':
                    prev = '0'
                else:
                    prev = '?'
                ans += (right - left) 
                right += 1
            else:
                if s[left] == '?' or s[right] == '?':
                    left = right - 1
                    prev = None
                else:
                    left = right
                    right += 1
        print('ans: ', ans)
    print(ans + n)