S = input()

curr_max, curr_min = S, S
for i in range(len(S)):
    temp = S[len(S) - i: len(S)] + S[:len(S) - i]
    curr_max = max(curr_max, temp)
    curr_min = min(curr_min, temp)

print(curr_min)
print(curr_max)