"""
even number of "
for each i = [1, K]
(2i - 1) to (2i) is enclosed
replace all , with . that are not enclosed

1st to 2nd, 3rd to 4th, ...

ex:
8
"a,b"c.d
count(") = 2, K = 1

for each enclosure, keep track of where , is
"""
N = int(input())
S = list(input())

flag = False
for i, c in enumerate(S):
    if c == '"' and not flag:
        flag = True
    elif c == '"' and flag:
        flag = False
    elif c == ',' and not flag:
        S[i] = "."

print("".join(S))
