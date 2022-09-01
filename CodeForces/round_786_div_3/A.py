def main():
    # make x = y by x = (b * x) * a
    # x * b^n so y must be divisible by x

    x, y = map(int, input().split())
    if y % x != 0:
        print(0, 0)
    else:
        print(1, y // x)


for _ in range(int(input())):
    main()