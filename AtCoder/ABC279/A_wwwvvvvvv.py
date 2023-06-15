S = input()
res = 0
for c in S:
    if c == "v":
        res += 1
    else:
        res += 2
print(res)
