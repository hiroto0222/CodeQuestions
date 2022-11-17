# diverse -> if count(s[i]) <= distinct_cnt
# max distinct chars -> 0, 1, 2, ... , 9 -> 10
# max length of distinct string -> 10 of each char -> 10^2 = 100
# for each starting point, check next 100 chars to see if distinct
# O(n * 10^2)


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0

    for i in range(n):
        j = i
        cnts = [0] * 10
        curr_max = 0
        distinct = 0

        while j < n and j - i + 1 <= 100:
            curr = int(s[j])
            if cnts[curr] == 0:
                distinct += 1
            cnts[curr] += 1
            curr_max = max(curr_max, cnts[curr])
            if curr_max <= distinct:
                ans += 1
            j += 1
    
    print(ans)