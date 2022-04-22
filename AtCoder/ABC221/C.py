from itertools import product

N = input()

ans = 0

for bit_combo in product((0, 1), repeat=len(N)):
    first, second = [], []
    for i, val in enumerate(bit_combo):
        if val == 1:
            first.append(N[i])
        else:
            second.append(N[i])
    
    if len(first) == 0 or len(second) == 0:
        continue
        
    first.sort(reverse=True)
    second.sort(reverse=True)
    a = int("".join(first))
    b = int("".join(second))
    ans = max(ans, a * b)

print(ans)
