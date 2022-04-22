"""
exactly one operation: choose a positive int m and multiply once to a, b, c
a -> b -> c (arithmetic) => x[i + 1] = x[i] + d

check c:
    d = b - a
    correct_c = 2b - a -> check if (2b - a) % c == 0
check b:
    2d = c - a
    d = (c - a) / 2
    correct_b = a + (c - a) / 2 -> check if (a + (c - a) / 2) % b == 0
check a:
    d = c - b
    correct_a = 2b - c -> check if (2b - c) % a == 0
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    
    # check c
    check_c = 2*b - a
    if (check_c >= c and check_c % c == 0 and check_c != 0):
        print("YES")
        continue
    
    # check b
    check_b = a + (c - a) / 2
    if (check_b >= b and check_b % b == 0 and check_b != 0):
        print("YES")
        continue

    # check a
    check_a = 2*b - c
    if (check_a >= a and check_a % a == 0 and check_a != 0):
        print("YES")
        continue
    
    print("NO")
