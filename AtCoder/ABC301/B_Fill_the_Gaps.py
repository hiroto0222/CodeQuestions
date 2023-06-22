# if abs(A[i] - A[i + 1]) == 1 end
# if A[i] < A[i + 1] insert

N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    print(A[i], end=" ")
    if abs(A[i] - A[i + 1]) != 1:
        if A[i] < A[i + 1]:
            for d in range(1, A[i + 1] - A[i]):
                print(A[i] + d, end=" ")
        elif A[i] > A[i + 1]:
            for d in range(1, A[i] - A[i + 1]):
                print(A[i] - d, end=" ")

print(A[-1], end="")
