N = int(input())
for k in range(10000):
    if (2**k > N):
        print(k - 1)
        break
