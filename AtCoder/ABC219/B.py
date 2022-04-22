S1 = input()
S2 = input()
S3 = input()
T = input()

ans = ""
for val in T:
    if val == "1":
        ans += S1
    elif val == "2":
        ans += S2
    else:
        ans += S3

print(ans)