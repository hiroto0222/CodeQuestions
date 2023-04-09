"""
init x = 0
00 -> x * 100
0 -> x * 10 + 0
...
9 -> x * 10 + 9

ex:
40004
4 -> 4
00 -> 400
0 -> 4000
4 -> 40004

ans = len(S) - count of double 0
"""

S = input()
res = len(S)
prev = S[0]
for i in range(1, len(S)):
    if S[i] == "0" and prev == "0":
        res -= 1
        prev = ""
    else:
        prev = S[i]

print(res)
