from math import comb as binom

def count_quadruples(N):
    if N % 2 == 1:
        # AB + CD is odd, so there are no solutions
        return 0

    M = N // 2  # consider AB + CD = M instead

    # compute the coefficient of x^M in G(x)
    coef = 0
    for k in range(1, int(M**0.5)+1):
        if M % k == 0:
            coef += k**2 * binom(2*k, k)**2
            if k != M//k:
                coef += (M//k)**2 * binom(2*(M//k), M//k)**2

    # multiply by 2^4 to get the total number of quadruples
    return coef * 16

N = int(input())
print(count_quadruples(N))