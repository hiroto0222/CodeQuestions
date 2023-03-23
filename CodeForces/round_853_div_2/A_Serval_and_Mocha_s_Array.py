def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    """
    find 2 vals such that gcd(a, b) <= 2
    then can always bring those 2 to front and produce good seq
    then rest are all good such that seq becomes beautiful
    """

    n = int(input())
    a = list(map(int, input().split()))

    ans = "No"
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) <= 2:
                ans = "Yes"
                break
    
    print(ans)