# where cut
# 1st -> 0
# 2nd -> A1 % 360
# 3rd -> A1 + A2 % 360
# 1. create array of cut positions
# 2. sort array of cut positions and + 360
# 3. obtain differences between A[i] and A[i + 1] and keep track of max


n = int(input())
A = list(map(int, input().split()))
cuts = [0]

curr_sum, curr_max = 0, 0

for val in A:
    curr_sum = (curr_sum + val) % 360
    cuts.append(curr_sum)

cuts.sort()
cuts.append(360)

for i in range(len(cuts) - 1):
    curr_max = max(curr_max, cuts[i + 1] - cuts[i])

print(curr_max)