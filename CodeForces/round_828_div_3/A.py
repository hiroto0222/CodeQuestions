for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    dic = {}
    ans = "YES"

    for i, val in enumerate(a):
        if val not in dic:
            dic[val] = s[i]
            continue
            
        if dic[val] != s[i]:
            ans = "NO"
            break
    
    print(ans)
