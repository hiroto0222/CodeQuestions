H, W = map(int, input().split())
S = list(input() for _ in range(H))
T = list(input() for _ in range(H))

for s_row, t_row in zip(S, T):
    if sorted(s_row) != sorted(t_row):
        print("No")
        exit()
print("Yes")
