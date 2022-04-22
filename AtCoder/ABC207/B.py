A, B, C, D = map(int, input().split())
for i in range(10**5 + 1):
    if (A + B*i) <= (D*i):
        print(i)
        exit()
print(-1)
