def main():
    s = input()
    t = input()

    if t == "a":
        print(1)
    elif t.count("a") != 0:
        print(-1)
    else:
        print(2 ** len(s))


for _ in range(int(input())):
    main()