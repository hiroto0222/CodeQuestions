N = int(input())
arr = ['AC', 'WA', 'TLE', 'RE']
dic = {k : 0 for k in arr}
for _ in range(N):
    curr = input()
    dic[curr] += 1

for key in dic.keys():
    print("{} x {}".format(key, dic[key]))
