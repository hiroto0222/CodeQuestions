N = int(input())

if (N < 42):
    curr = str(N)
else:
    curr = str(N + 1)

print("AGC" + "0" * (3 - len(curr)) + curr)