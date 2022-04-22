for _ in range(int(input())):
    n = int(input())

    seen = set()
    for i in range(1, int(n**0.5) + 1):
        if i**2 <= n:
            seen.add(i**2)
        if i**3 <= n:
            seen.add(i**3)
    
    print(len(seen))