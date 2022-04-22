# X yen
# tot >= Y
X, Y = map(int, input().split())
if X >= Y:
    print(0)
else:
    if (Y - X) % 10 > 0:
        Y += (10 - (Y - X) % 10)
    print((Y - X) // 10)