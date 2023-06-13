N = int(input())

if N % 5 == 0:
    print(N)
else:
    x = (N // 5) * 5
    y = (N // 5 + 1) * 5
    if abs(x - N) > abs(y - N):
        print(y)
    else:
        print(x)
