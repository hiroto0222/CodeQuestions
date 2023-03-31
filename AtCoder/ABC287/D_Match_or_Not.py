"""
for each x = 0, 1, ... , T
if S[:x] + S[T - x:] = T

a??bc
b???
x = 0 -> _ + ??bc
x = 1 -> a + ?bc
x = 2 -> a? + bc
x = 3 -> a?? + c
x = 4 -> a??b + _

ex:
a?c, 3
b?,  2

x = 0
?c, b?

x = 1
ac, b?

x = 2
a?, b?

create backward and forward True False
"""

S = input()
T = input()
len_S = len(S)
len_T = len(T)

pre, post = [False] * (len_T + 1), [False] * (len_T + 1)
pre[0], post[0] = True, True

for i in range(1, len_T + 1):
    if not pre[i - 1]: break
    if S[i - 1] == "?" or T[i - 1] == "?" or S[i - 1] == T[i - 1]:
        pre[i] = True

for i in range(1, len_T + 1):
    if not post[i - 1]: break
    if S[len_S - i] == "?" or T[len_T - i] == "?" or S[len_S - i] == T[len_T - i]:
        post[i] = True

for x in range(len_T + 1):
    if pre[x] and post[len_T - x]:
        print("Yes")
    else:
        print("No")