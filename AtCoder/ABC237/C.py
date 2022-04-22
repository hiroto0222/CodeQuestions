# aabbba -> No
# aaabbbaaaa

S = input()

if (len(S) == 1 or len(set(S)) == 1):
    print("Yes")
    exit()

ans = "No"
l, r = 0, len(S) - 1
while (l < r):
    if S[l] == "a":
        l += 1
    if S[r] == "a":
        r -= 1
    if S[l] != "a" and S[r] != "a":
        if (len(S) - r - 1) < l:
            break
        if (S[l:r+1][::-1] == S[l:r+1]):
            ans = "Yes"
            break
        else:
            break

print(ans)