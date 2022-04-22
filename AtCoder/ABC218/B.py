P = list(map(int, input().split()))

ans = ""
for num in P:
    ans += chr(97 + (num - 1))
print(ans)