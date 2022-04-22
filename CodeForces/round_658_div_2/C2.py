for _ in range(int(input())):
    n = int(input())
    a = input() + '0'
    b = input() + '0'

    ans = []
    for i in range(n):
        if a[i] != a[i + 1]:
            ans.append(i + 1)
    
    for i in range(n - 1, -1, -1):
        if b[i] != b[i + 1]:
            ans.append(i + 1)
    
    print(len(ans), *ans)