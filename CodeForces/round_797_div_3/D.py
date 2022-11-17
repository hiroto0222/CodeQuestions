# sliding window

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    curr_replaces = sum([s[i] == "W" for i in range(k)])
    ans = curr_replaces
    for i in range(n - k):
        curr_replaces += (s[i + k] == "W") - (s[i] == "W")
        ans = min(ans, curr_replaces)
    
    print(ans)
