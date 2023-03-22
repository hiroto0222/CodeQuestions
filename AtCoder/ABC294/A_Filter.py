n = int(input())
a = list(map(int, input().split()))
res = []
for val in a:
    if val % 2 == 0:
        res.append(val)
print(*res)