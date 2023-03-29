"""
S = 20230322

if num of vals in seq are even, then good
to keep track of number of vals, create prefix sum

take % 2
0 -> [0,1,1,1,2,2,2,2] -> [0,1,1,1,0,0,0,0]
2 -> [1,1,2,2,2,2,3,4] -> [1,1,0,0,0,0,1,0]
3 -> [0,0,0,1,1,2,2,2] -> [0,0,0,1,1,0,0,0]
for a sub sequence [l, r] to be good, cnts[l][1~9] == cnts[r][1~9]
for example if 3 cases of 010 -> 3C2 -> n(n - 1) / 2 -> 6
"""
from collections import defaultdict

S = input()
prefix_sum = [0]*10  # prefix sum of 0~9
dic = defaultdict(int)
curr = "0"*10
dic[curr] += 1

for i in range(len(S)):
    prefix_sum[int(S[i])] += 1
    prefix_sum[int(S[i])] %= 2
    curr = "".join(map(str, prefix_sum))
    dic[curr] += 1

res = 0
for x in dic:
    n = dic[x]
    res += n * (n - 1) // 2

print(res)