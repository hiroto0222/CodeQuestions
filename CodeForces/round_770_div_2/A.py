"""
if rev(s) == s then 1
else
    rev(s) + s -> palindrome1
    s + rev(s) -> palindrome2
    always 2 different strings
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    if (s[::-1] == s or k == 0):
        print(1)
    else:
        print(2)