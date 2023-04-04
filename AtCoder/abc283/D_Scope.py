"""
good string if can make empty string by:
1. first remove all english letters
2. then repeatedly remove consecutive ( )

ex:
(a(ba))

i = 0 ->


keep a stack for the largest j such that when S[i] = ), S[j:i] forms a good string
"""
from collections import defaultdict

S = input()

prev_bracket = 0
chars = defaultdict(list)  # keep track of chars in curr good seq
curr_used = [False] * 26
for i in range(len(S)):
    c = S[i]

    if c == "(":
        prev_bracket += 1

    elif c == ")":
        for char in chars[prev_bracket]:
            curr_used[ord(char) - ord("a")] = False
        chars[prev_bracket].clear()
        prev_bracket -= 1

    else:
        if curr_used[ord(c) - ord("a")]:
            print("No")
            exit()
        chars[prev_bracket].append(c)
        curr_used[ord(c) - ord("a")] = True

print("Yes")
