"""
p^2 * q = N
in the case p = q -> p^3 = N
            min(p, q) <= N^1/3
hence iterate all possible primes between [2, N^1/3] using Sieve Of Eratosthenes
if N % prime == 0:
    if N % (prime**2) == 0:
        p = prime, q = N // p**2
    else:
        q = prime, int((N // prime)**(1/2))
"""
MAX_N = 9 * 10**18

def get_primes(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= N):
        if is_prime[p]:
            for i in range(p * p, N + 1, p):
                is_prime[i] = False
        p += 1
    
    return is_prime

is_primes = get_primes(int(MAX_N**(1 / 3)))
primes = [i for i in range(int(MAX_N**(1 / 3))) if is_primes[i]]

for _ in range(int(input())):
    N = int(input())
    for prime in primes:
        if N % prime == 0:
            if N % prime**2 == 0:
                p = prime
                q = N // (prime**2)
            else:
                q = prime
                p = int((N // prime)**(1 / 2))
            break
    print(p, q)