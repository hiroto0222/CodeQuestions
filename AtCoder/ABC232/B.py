S = input()
T = input()

ans = "No"
for k in range(26):
    temp = ""
    for i in range(len(S)):
        temp += chr(ord("a") + (ord(S[i]) + k) % 26)
    if temp == T:
        ans = "Yes"
        break

print(ans)