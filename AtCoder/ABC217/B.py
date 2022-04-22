S1 = input()
S2 = input()
S3 = input()

print(*[val for val in ["ABC", "ARC", "AGC", "AHC"] if val not in [S1, S2, S3]])