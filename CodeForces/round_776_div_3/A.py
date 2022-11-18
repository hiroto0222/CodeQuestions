for _ in range(int(input())):
    s = input()
    c = input()

    if c not in s:
        print("NO")
        continue
    
    ans = "NO"
    for i in range(len(s)):
        if (s[i] == c) and (i % 2 == 0):
            ans = "YES"
            break
    print(ans)