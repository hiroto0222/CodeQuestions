from bisect import bisect_left, bisect_right
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    print(a)
    for i in range(n):
        print('for: ', a[i])
        print('find: {} and {}'.format(l - a[i], r - a[i]))
        left_idx = bisect_left(a, l - a[i], i + 1, n)
        right_idx = bisect_right(a, r - a[i], i + 1, n)
        print('left : {}, right: {}'.format(left_idx, right_idx))
        ans += (right_idx - left_idx)
        print('\n')
    print(ans)
