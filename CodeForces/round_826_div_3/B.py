# funny permutation
# for i -> abs(a[i - 1] - a[i]) == 1 or abs(a[i + 1] - a[i]) == 1
# for i -> i != a[i]


for _ in range(int(input())):
    n = int(input())
    
    if n == 2:
        print(2, 1)
        continue
    
    if n == 3:
        print(-1)
        continue
    
    perms = [1, 2]
    left = [i for i in range(3, n + 1)]
    print(*(left + perms))