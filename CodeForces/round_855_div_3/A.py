import re

def compute(s):
    return bool(re.match(r'^[mM]+[eE]+[oO]+[wW]+$', s))

for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    if compute(s): print("Yes")
    else: print("No")