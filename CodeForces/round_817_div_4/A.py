def main():
    n = int(input())
    s = input()
    valid = set(["T", "i", "m", "u", "r"])

    for char in s:
        if char in valid:
            valid.remove(char)
        else:
            return "NO"

    return "YES" if not valid else "NO"

for _ in range(int(input())):
    print(main())