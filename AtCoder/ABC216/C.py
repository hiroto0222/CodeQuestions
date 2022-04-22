"""
A -> add 1 ball to box
B -> 2 x balls in box
steps <= 120
make balls = N

if N is even -> B(A x N // 2)
if N is odd -> B(A x (N - 1) // 2)B
"""

N = int(input())
ans = ""
while (N > 0):
    if (N % 2):
        ans += "A"
        N -= 1
    else:
        ans += "B"
        N //= 2

print(ans[::-1])