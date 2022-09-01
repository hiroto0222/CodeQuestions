def main():
    # 1 -> ab
    # 25 -> az
    # 26 -> ba
    # 51 -> ca, 75 -> cz
    # 1 + 25 * (letter index) -> letter + "a"
    # za -> 626
    # zy -> 626

    s = input()
    ans = 0
    ans += 1 + (ord(s[0]) - 97) * 25
    if (s[1] > s[0]):
        ans += ord(s[1]) - 97 - 1
    else:
        ans += ord(s[1]) - 97

    print(ans)


for _ in range(int(input())):
    main()