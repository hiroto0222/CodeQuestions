def main():
    keyboard = input()
    s = input()
    ans = 0

    if (len(s) == 1):
        print(ans)
        return
    
    prev = keyboard.index(s[0])
    for i in range(1, len(s)):
        ans += abs(keyboard.index(s[i]) - prev)
        prev = keyboard.index(s[i])

    print(ans)
    return


for _ in range(int(input())):
    main()