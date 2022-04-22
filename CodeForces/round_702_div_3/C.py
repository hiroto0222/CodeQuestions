import math

t = int(input())
for _ in range(t):
    x = int(input())
    max_a = math.ceil((x / 2) ** (1 / 3))
    ans = 'NO'

    for a in range(1, max_a + 1):
        val = x - a**3
        if val < 0:
            continue
        else:
            val = abs(val)
            if (round(val ** (1 / 3)) ** 3) == val and val >= 1:
                ans = 'YES'
                break

    print(ans)
