"""
Kth S means, there are K iterations before

A - Z -> 26**1
AA - ZZ -> 26**2 
AAA - ZZZ -> 26**3

ie: AAAA -> 26**1 + 26**2 + 26**3

BEAN:
before B -> A??? = 26**3 * A(1)
before E -> BA??
            BB??
            BC??
            BD?? = 26**2 * D(4)
before A -> nth  = 26**1 * 0
before N -> BEAA
            ...
            BEAM = 26**0 * M(13)
BEAN = AAAA + above
BEAN = (26^3 + 26^2 + 26^1 + 26^0) + (26^3 + 26^2 * 4 + 26^1 * 0 + 26^0 * 13)
"""

S = input()
N = len(S)
res = 0
for i in range(N):
    char = S[i]
    res += 26**(N - i - 1) + 26**(N - i - 1) * (ord(char) - ord("A"))
print(res)