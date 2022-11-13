# invert subtrees to sort leaves
# can only alter by groups of 2^n
# 6 5 7 8 4 3 1 2 -> 6 5, 7 8, 4 3, 1 2


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x, ans = 1, 0

    while x < n:
        for i in range(0, n, 2*x):
            if abs(arr[i] - arr[i + x]) != x:
                ans = -1
                break
            if arr[i] > arr[i + x]:
                arr[i], arr[i + x] = arr[i + x], arr[i]
                ans += 1
        x *= 2
        if ans == -1:
            break
    
    print(ans)