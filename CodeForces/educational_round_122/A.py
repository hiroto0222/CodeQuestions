def main():
    n = int(input())
    if n % 7 == 0:
        print(n)
        return

    for j in range(10):
        if (n - n % 10 + j) % 7 == 0:
            ans = n - n % 10 + j
            break
    
    print(ans)

for _ in range(int(input())):
    main()