"""
left -> x - d
right -> x + d

if curr x is even -> left
if curr x is odd -> right

0 1 -> -1 
0 2 -> -1 -> 1

if x is even
2, 6, 10, ... = x + 1
4, 8, 12, ... = x
10 10 -> 9 odd -> 11 odd -> 14 even -> 10 even -> 5 odd -> 11 odd -> 18 even -> 10 even -> 1 odd -> 11 odd -> 22 even -> 10 even

if x is odd
2, 6, 10, ... = x - 1
4, 8, 12, ... = x
-1, 1 -> 0 even -> -2 even -> -5 odd -> -1 odd -> 4 even -> -2 even -> -9 odd -> -1 odd -> 8 even
"""


def main():
    x, n = map(int, input().split())

    if (n == 1):
        if (x % 2 == 0):
            print(x - 1)
        else:
            print(x + 1)
        return

    if (x % 2 == 0):
        if (n % 2 == 0):
            if (n % 4 == 0):
                print(x)
            else:
                print(x + 1)
        else:
            if ((n - 1) % 4 == 0):
                print(x - n)
            else:
                print(x + 1 + n)
    else:
        if (n % 2 == 0):
            if (n % 4 == 0):
                print(x)
            else:
                print(x - 1)
        else:
            if ((n - 1) % 4 == 0):
                print(x + n)
            else:
                print(x - 1 - n)


for _ in range(int(input())):
    main()