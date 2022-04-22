def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

n = int(input())
seen = set()

while n not in seen:
    seen.add(n)
    n = f(n)

print(len(seen))