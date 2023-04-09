"""
K >= 2
find N such that N! = K * x, where N is minimum

eg:
K = 30
5! -> 120 // 30 -> N = 5

Every integer n > 1 has a unique factorization as product of primes
n = (p1^a1)(p2^a2)(p3^a3)...(pm^am)
When X is a multiple of K, then X is a multiple of some pi^ai

1. find unique prime factorizations of K
2. for each i = [1, m], let N_i! be the minimum multiple of p_i^a_i
3. N = max(N1, N2 ..., Nm)

eg:
30 = 2 * 3 * 5
then N! / 2, N! / 3, N! / 5 must hold

or for B to be divisible by A
A = 2^(a1) + 3^(a2) + 5^(a3) ...
B = 2^(b1) + 3^(b2) + 5^(b3) ...
where b1 >= a1, b2 >= a2, b3 >= a3, ...
"""
import math


def main():
    K = int(input())
    facts = factorization(K)
    res = binary_search(facts)
    print(res)


def factorization(n):
    """Return list of prime factors with counts, [prime_factor, cnt]"""
    arr = []
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp > 2:
        arr.append([temp, 1])

    if not arr:
        arr.append([n, 1])

    return arr


def binary_search(facts):
    lo, hi = 1, 10**12

    def is_ok(x, p, c):  # where (p, c) is from facts of K
        cnt = 0
        while x:
            x //= p
            cnt += x

        return cnt >= c

    while hi - lo > 1:
        mid = (hi + lo) // 2
        for p, c in facts:
            if not is_ok(mid, p, c):
                lo = mid
                break
        else:
            hi = mid

    return hi


if __name__ == "__main__":
    main()
