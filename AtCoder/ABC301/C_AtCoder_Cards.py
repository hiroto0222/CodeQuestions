# card has alphabet or "@"
# game:
# 1. order cards in group of 2 equal lengths
# 2. replace "@" with any "atcoder"
# 3. check if groups are equal

from collections import Counter

S = input()
T = input()
S_cnt = Counter(S)
T_cnt = Counter(T)

for c in "atcoder":
    cnt = max(S_cnt[c], T_cnt[c])
    if S_cnt["@"] < cnt - S_cnt[c] or T_cnt["@"] < cnt - T_cnt[c]:
        print("No")
        exit()

    S_cnt["@"] -= cnt - S_cnt[c]
    S_cnt[c] = cnt
    T_cnt["@"] -= cnt - T_cnt[c]
    T_cnt[c] = cnt

print("Yes" if S_cnt == T_cnt else "No")
