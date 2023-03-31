"""
A cost -> S[1]S[2]...S[N] -> S[2]S[3]...S[N]S[1]
B cost -> S[i] = alphabet
min cost to convert S to palindrome

ex:
5 1 2
rrefa

A = 1 -> refar
B = 2 -> refer

if N is even -> must have even counts for each letter
if N is odd -> 1 must have odd count, others have even

rotate every possible -> O(N)
    for each possible, check how many letters need to be changed to create palindrome O(N)
O(N^2)
"""

N, A, B = map(int, input().split())
S = list(input())
curr_min = float('inf')

for i in range(N):
    curr = A*i
    for j in range(N // 2):
        if S[j] != S[N - j - 1]:
            curr += B
    curr_min = min(curr_min, curr)
    S.append(S.pop(0))

print(curr_min)