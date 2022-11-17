# a -> a[i] = a[i] - 1 if a[i] > 0 for each

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    curr_steps = -1
    min_zero_steps = 0
    ans = "YES"
    for i in range(n):
        curr = a[i] - b[i]
        if curr < 0:
            ans = "NO"
            break
        if b[i] == 0:
            min_zero_steps = max(min_zero_steps, a[i] - b[i])
        else:
            if curr_steps == -1:
                curr_steps = a[i] - b[i]
            else:
                if a[i] - b[i] != curr_steps:
                    ans = "NO"
                    break
    
    if curr_steps == -1:
        print(ans)
        continue

    if ans == "YES" and min_zero_steps <= curr_steps: print("YES")
    else: print("NO")