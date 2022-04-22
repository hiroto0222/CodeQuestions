x = list(map(int, input().split(".")))
if (x[1] <= 2):
    print(str(x[0]) + "-")
elif (3 <= x[1] <= 6):
    print(str(x[0]))
else:
    print(str(x[0]) + "+")