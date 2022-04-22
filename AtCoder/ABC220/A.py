A, B, C = map(int, input().split())
for i in range(1, 1001):
    if C*i > B:
        print(-1)
        break

    if C*i >= A and C*i <= B:
        print(C*i)
        break
