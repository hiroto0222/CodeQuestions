K = int(input())
A, B = input().split()

x = 0
for i in range(len(A)):
    x += (int(A[i]))*K**(len(A) - i - 1)

y = 0
for i in range(len(B)):
    y += (int(B[i]))*K**(len(B) - i - 1)

print(x * y)