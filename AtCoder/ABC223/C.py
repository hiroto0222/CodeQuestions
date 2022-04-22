N = int(input())
arr = []
time_taken = 0

for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
    time_taken += a / b

left_time = time_taken / 2
ans = 0

for a, b in arr:
    if left_time >= a / b:
        ans += a
        left_time -= a / b
    else:
        ans += left_time * b
        break

print(ans)