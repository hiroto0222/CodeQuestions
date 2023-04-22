N = int(input())
S = input()
braks = []
for i, c in enumerate(S):
    if c == "|":
        braks.append(i)
print("in" if S.index("*") > braks[0] and S.index("*") < braks[1] else "out")
