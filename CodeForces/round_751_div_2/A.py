def main():
    s = list(input())
    a = s.index(min(s))
    b = ""
    for i in range(len(s)):
        if i != a:
            b += s[i]
    print(s[a], b)


for _ in range(int(input())):
    main()