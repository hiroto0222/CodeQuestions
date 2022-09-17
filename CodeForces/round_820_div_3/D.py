for _ in range(int(input())):
    # maximize groups -> make each group exactly 2

    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    arr = [y[i] - x[i] for i in range(n)]
    arr.sort(reverse=True)

    if arr[1] + arr[0] < 0:
        # if the largest sum of diff is smaller than 0, no pairs can be formed
        print(0)
        continue

    i, j, cnt = 0, n - 1, 0
    while i < j:
        if -1 * arr[j] > arr[i]:
            j -= 1
        else:
            cnt += 1
            i += 1
            j -= 1

    print(cnt)