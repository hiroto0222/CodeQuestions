def main():
    a, b, c = map(int, input().split())
    print(max(0, max(b, c) - a + 1), max(0, max(a, c) - b + 1), max(0, max(a, b) - c+ 1))


for _ in range(int(input())):
    main()