# all strings start with either H, D, C, S
# all strings end with either A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , T , J , Q , K
# all strings are unique

N = int(input())
S = list(input() for _ in range(N))

seen = set()
for s in S:
    if s in seen:
        print("No")
        exit()

    seen.add(s)
    if s[0] not in ["H", "D", "C", "S"]:
        print("No")
        exit()
    if s[1] not in [
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "T",
        "J",
        "Q",
        "K",
    ]:
        print("No")
        exit()

print("Yes")
