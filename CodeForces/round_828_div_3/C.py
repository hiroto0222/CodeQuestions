# find max distance from c to 'g'
# n - c_idx + g_idx
# want first g_idx such that g_idx >= c_idx else n - c_idx + min(g_idx)

from bisect import bisect_left

for _ in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input()

    c_idxs = []
    g_idxs = []
    curr_max = 0

    for i, char in enumerate(s):
        if char == c: c_idxs.append(i)
        if char == 'g': g_idxs.append(i)
    
    for c_idx in c_idxs:
        pos = bisect_left(g_idxs, c_idx)
        if pos < len(g_idxs):
            curr_max = max(curr_max, g_idxs[pos] - c_idx)
        else:
            curr_max = max(curr_max, n - c_idx + g_idxs[0])
    
    print(curr_max)