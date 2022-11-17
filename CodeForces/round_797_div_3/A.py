# x is lowest -> x + 1, x + 2, x
# n = 11 -> 8


for _ in range(int(input())):
    n = int(input())
    x = (n - 3) // 3
    left = n - 3 * x
    
    if left % 2 == 0:
        print(x + left // 2 - 1, x + left // 2 + 1, x)
    else:
        print(x + left // 2, x + left // 2 + 1, x)