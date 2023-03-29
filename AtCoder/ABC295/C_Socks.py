N = int(input())
A = list(map(int, input().split()))
seen = set()
res = 0

for val in A:
    if val in seen:
        seen.remove(val)
        res += 1
    else:
        seen.add(val)

print(res)