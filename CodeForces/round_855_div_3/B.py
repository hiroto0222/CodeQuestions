from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = 0

    for i in range(26):
        c = chr(ord("a") + i)
        lower_cnt = s.count(c)
        upper_cnt = s.count(c.upper())
        ans += min(lower_cnt, upper_cnt)
        diff = min(k, abs(lower_cnt - upper_cnt) // 2)
        k -= diff
        ans += diff

    print(ans)