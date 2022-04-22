"""
each step, remove 1 digit
min steps so that n % 25 == 0 and n > 0
00 25 50 75
"""

def main():
    n = input()
    ans = len(n)
    accepted = ["00", "25", "50", "75"]
    for accept in accepted:
        idx = 1
        for i in range(len(n) - 1, -1, -1):
            if (accept[idx] == n[i]):
                idx -= 1
            if (idx == -1):
                ans = min(ans, len(n) - i - 2)
                break
    
    print(ans)

    
for _ in range(int(input())):
    main()