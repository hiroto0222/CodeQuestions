# size -> "M", "X"*n + "S" or "L"

for _ in range(int(input())):
    a, b = input().split()
    
    if a[-1] == b[-1]:
        if len(a) == len(b):
            print("=")
        elif a[-1] == "S":
            print(">" if len(a) < len(b) else "<")
        elif a[-1] == "L":
            print(">" if len(a) > len(b) else "<")
    else:
        print(">" if a[-1] < b[-1] else "<")