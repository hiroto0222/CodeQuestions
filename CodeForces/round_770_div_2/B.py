"""
start with number d and do dollowing task
    1. d = d + a[i]
    2. d = d XOR a[i]

    x (even)    -> 110...000 ^ 010...000 (even) = ...000 (even)
                -> 110...000 ^ 010...001 (odd) = ...001 (odd)

    x + 3 (odd) -> 110...001 ^ 010...000 (even) = ...001 (odd)
                -> ......001 ^ 010...001 (odd) = ...000 (even)
    
    cnt number of odd numbers -> if cnt % 2 == 0 then no parity change
                              -> if cnt % 2 != 0 then parity change
"""

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    cnt_odd = 0
    for val in a:
        if val % 2 != 0:
            cnt_odd += 1
    
    if (cnt_odd % 2 == 0):
        if (y % 2 == x % 2):
            print("Alice")
        else:
            print("Bob")
    else:
        if (y % 2 != x % 2):
            print("Alice")
        else:
            print("Bob")