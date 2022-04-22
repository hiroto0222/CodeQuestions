t = int(input())
for _ in range(t):
    n = int(input())
    chars = input()
    seen = set()
    prev = False
    for char in chars:
        if not prev:
            prev = char
        elif char != prev and char in seen:
            print('NO')
            break
        seen.add(char)
        prev = char
    else:
        print('YES')
