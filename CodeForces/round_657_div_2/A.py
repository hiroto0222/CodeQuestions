for _ in range(int(input())):
    n = int(input())
    s = input()

    sub_str = 'abacaba'
    s_replace = s.replace('?', 'd')
    cnt = 0
    for i in range(len(s_replace)):
        if s_replace[i:i + 7] == sub_str:
            cnt += 1
    
    if cnt == 1:
        ans = 'Yes'
        print(ans)
        print(s_replace)
        continue
    elif cnt > 1:
        ans = 'No'
        print(ans)
        continue
    
    ans = 'NO'
    for i in range(n):
        arr = list(s)
        ok = True
        for j in range(len(sub_str)):
            if i + j < len(arr) and (arr[i + j] == '?' or arr[i + j] == sub_str[j]):
                arr[i + j] = sub_str[j]
            else:
                ok = False
                break
        
        if not ok:
            continue

        s_replace = "".join(arr).replace('?', 'd')

        if s_replace.count(sub_str) == 0:
            continue

        cnt = 0
        for i in range(len(s_replace)):
            if s_replace[i:i + 7] == sub_str:
                cnt += 1
            
            if cnt > 1:
                break
        
        if cnt == 1:
            ans = 'YES'
            print(ans)
            print(s_replace)
            break
    else:
        print(ans)
