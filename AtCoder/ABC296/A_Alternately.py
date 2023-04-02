N = int(input())
S = input()
prev = S[0]
for i in range(1, N):
    if S[i] == prev:
        print("No")
        exit()
    prev = S[i]
print("Yes")