def main():
    # G = B

    n = int(input())
    s1 = input()
    s2 = input()

    for i in range(n):
        char1, char2 = s1[i], s2[i]
        if (char1 == "G" and char2 == "R") or (char1 == "B" and char2 == "R"):
            return "NO"
        if (char1 == "R" and char2 == "G") or (char1 == "R" and char2 == "B"):
            return "NO"

    return "YES"


for _ in range(int(input())):
    print(main())