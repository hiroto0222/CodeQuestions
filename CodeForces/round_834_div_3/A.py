for _ in range(int(input())):
    s = input()
    x = "Yes"
    curr = s[0]
    if curr not in x:
        print("No")
        continue

    l = x.index(curr)
    ans = "Yes"
    for i in range(len(s)):
        if x[l] != s[i]:
            ans = "No"
            break
        l = (l + 1) % 3

    print(ans)
