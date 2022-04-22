N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)
cnt = X // sum_A * len(A)
tot = X // sum_A * sum_A

for i in range(len(A)):
    cnt += 1
    tot += A[i]
    if tot > X:
        print(cnt)
        break
