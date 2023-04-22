"""
As S[l] = 0 and S[r] = 1
there exists p such that S[p] = 0 and S[p + 1] = 1
binary search where
1. if S[m] = 0, then l = m, r = r
2. if S[m] = 1, then r = m, l = l
until l + 1 = r

N = 200000
O(lg N) <= 18
thus can solve in at most 20 questions
"""

N = int(input())
l, r = 0, N - 1

while True:
    m = (l + r) // 2
    print(f"? {m + 1}", flush=True)
    S = input()
    if S == "0":
        l = m
    else:
        r = m

    if r == l + 1:
        print(f"! {l + 1}", flush=True)
        exit()
