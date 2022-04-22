from heapq import heapify, heappop, heappush

t = int(input())
for _ in range(t):
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    data = {}
    for i, uni in enumerate(u):
        if uni not in data:
            curr = [-s[i]]
            heapify(curr)
            data[uni] = curr
        else:
            heappush(data[uni], -s[i])
    
    ans = [0]*n

    for curr_uni in data.values():
        curr_uni_len = len(curr_uni)
        
        sums = [0]*curr_uni_len
        curr_sum = 0
        for i in range(curr_uni_len):
            curr_sum -= heappop(curr_uni)
            sums[i] = curr_sum

        for k in range(1, n + 1):
            if k > curr_uni_len:
                break
            else:
                if curr_uni_len % k == 0:
                    ans[k - 1] += sums[-1]
                else:
                    remains = curr_uni_len % k
                    ans[k - 1] += sums[curr_uni_len - remains - 1]

    print(*ans)

