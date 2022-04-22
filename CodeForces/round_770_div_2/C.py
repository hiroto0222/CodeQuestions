"""
n*k total items
n -> shelves
k -> items per shelf
for each i, l, r -> (a[i][l:] + a[i][:r]) / (r - l) % 1 == 0
find out if possible

1, 3, 5, 7, 9
11, 13, 15, 17, 19
2, 4, 6, 8, 10
"""

def main():
    n, k = map(int, input().split())

    if k == 1:
        print("YES")
        for i in range(1, n + 1):
            print(i)
        return
    
    if (n % 2 == 1):
        print("NO")
        return
    
    print("YES")
    for i in range(1, n + 1):
        print(*[j for j in range(i, n * k + 1, n)])


for _ in range(int(input())):
    main()
        
