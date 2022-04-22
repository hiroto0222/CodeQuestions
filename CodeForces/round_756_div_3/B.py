"""
each team 4 students
each team atleast 1 A and 1 B
each team 1A + 1B + 2A or 1A + 1B + 2B or 2A + 2B
5 7

"""

def main():
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if (b - a == 0):
        print(a // 2)
    else:
        if a % 2 != 0 and b - a > 1:
            print(a // 2 + 1)
        else:
            print(a // 2)


for _ in range(int(input())):
    main()