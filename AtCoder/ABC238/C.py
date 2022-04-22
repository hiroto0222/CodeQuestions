# f(x) = all positive ints <= x with same number of digits as x
# f(1 - 9) = 1 to 9
# f(10 - 99) = 1 to 90
# f(100 - 999) = 1 to 900
# f(1000 - 9999) = 1 to 9000
# sum = (1 + N)*N / 2

n = int(input())
ans = 0
for i in range(1, len(str(n)) + 1):
    curr = min(n, 10**i - 1) - (10**(i - 1) - 1)
    ans += (curr*(curr + 1)) // 2

print(ans % 998244353)
