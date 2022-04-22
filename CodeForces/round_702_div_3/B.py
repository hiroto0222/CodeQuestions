t = int(input())
for _ in range(t):
    n = int(input())
    count = {0: 0, 1: 0, 2:0}
    ans = 0
    for val in list(map(int, input().split())):
        count[val % 3] += 1
    
    flag = False
    while not flag:
        max_key = max(count, key=count.get)
        prev = count[max_key]
        for key in count.keys():
            if prev != count[key]:
                break
            prev = count[key]
        else:
            flag = True
        if not flag:
            count[max_key] -= 1
            count[(max_key + 1) % 3] += 1
            ans += 1
    
    print(ans)
            
    

        