def main():
    # round to nearest 10
    # 178 -> 100 -> 78

    m = int(input())

    k = 1
    curr = 1
    while m >= 10**k:
        curr = 10**k
        k += 1

    return m - curr

for _ in range(int(input())):
    print(main())