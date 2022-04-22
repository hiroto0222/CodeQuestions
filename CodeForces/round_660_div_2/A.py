# consider first 3 smallest nearly prime numbers

for _ in range(int(input())):
    n = int(input())

    if n < 31:
        print("NO")
    elif (n - 30) in [6, 10, 14]:
        print("YES")
        print(14, 15, 6, (n - 35))
    else:
        print("YES")
        print(14, 10, 6, (n - 30))

for i in range(int(input())):
    print(i, " done")

for j, val in enumerate()