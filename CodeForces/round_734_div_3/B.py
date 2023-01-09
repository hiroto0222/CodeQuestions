# wonderful if
# - each letter of string is either red, green or none
# - each 2 letters painted in the same color are different
# - num of letters red == num of letters green
# - num of painted letters is max according to above 3 conds

from collections import Counter

for _ in range(int(input())):
    s = input()
    
    cnts = Counter(s)

    painted = 0
    for c in cnts.keys():
        painted += min(cnts[c], 2)
    
    if painted % 2 != 0:
        painted -= 1
    
    print(painted // 2)