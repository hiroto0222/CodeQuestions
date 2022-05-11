# given arrays A, B
# find array X[0, ..., N] such that
#  all X[i] == A[i] or B[i]
#  abs(X[i] - X[i + 1]) <= K

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a_ok, b_ok = True, True
    
    for i in range(N - 1):
        a_prev, a_curr = A[i], A[i + 1]
        b_prev, b_curr = B[i], B[i + 1]
        na_ok, nb_ok = False, False

        if a_ok:
            na_ok |= abs(a_prev - a_curr) <= K
            nb_ok |= abs(a_prev - b_curr) <= K
        if b_ok:
            na_ok |= abs(b_prev - a_curr) <= K
            nb_ok |= abs(b_prev - b_curr) <= K
        
        a_ok, b_ok = na_ok, nb_ok
    
    return a_ok or b_ok

print("Yes" if solve() else "No")