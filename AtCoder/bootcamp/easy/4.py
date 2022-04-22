N = int(input())

if (N / 1.08 % 1 == 0):
    print(int(N / 1.08))
else:
    if int(((N // 1.08) + 1) * 1.08) == N:
        print(int((N // 1.08) + 1))
    else:
        print(":(")