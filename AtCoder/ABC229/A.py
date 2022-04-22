S1 = input()
S2 = input()

if S1 == "##" or S2 == "##":
    print("Yes")
else:
    if S1 == ".#" and S2 == ".#":
        print("Yes")
    elif S1 == "#." and S2 == "#.":
        print("Yes")
    else:
        print("No")