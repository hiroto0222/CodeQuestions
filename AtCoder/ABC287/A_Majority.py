N = int(input())
x, y = 0, 0
for _ in range(N):
    S = input()
    if S == "For": x += 1
    else: y += 1

print("Yes" if x > y else "No")