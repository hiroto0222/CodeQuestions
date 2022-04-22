A, B = input().split()

A = A[::-1]
B = B[::-1]
ans = "Easy"
for i in range(len(min(A, B, key=len))):
    if (int(A[i]) + int(B[i]) > 9):
        ans = "Hard"
        break

print(ans)