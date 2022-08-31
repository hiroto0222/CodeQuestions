for _ in range(int(input())):
    # check if train can travel from q[0] -> q[1]
    # dp
    # dp[i] -> index of ith station, -1 if DNE

    input()
    n, k = map(int, input().split())
    routes = list(map(int, input().split()))

    dic = {}
    for i, route in enumerate(routes):
        if route not in dic:
            dic[route] = [i, i]
        else:
            dic[route][1] = i
        
    for _ in range(k):
        a, b = map(int, input().split())
        
        if a in dic and b in dic and dic[a][0] < dic[b][1]:
            print("YES")
        else:
            print("NO")