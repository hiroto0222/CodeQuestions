# segment -> a[l, r] = [a[l], a[l + 1], ..., a[r - 1], a[r]]
# each element only in 1 segment
# each segment sum equals
# want minimum max length
# 2 pointer 


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    curr_sum = 0
    curr_min = n + 1
    
    for i in range(n):
        curr_sum += a[i]
        curr_max = i + 1
        temp_sum, temp_cnt = 0, 0
        for j in range(i + 1, n):
            temp_sum += a[j]
            temp_cnt += 1
            if temp_sum == curr_sum:
                curr_max = max(curr_max, temp_cnt)
                temp_cnt = 0
                temp_sum = 0

        if temp_sum == 0:
            curr_min = min(curr_min, curr_max)
    
    print(curr_min)