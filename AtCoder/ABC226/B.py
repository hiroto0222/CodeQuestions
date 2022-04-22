N = int(input())
lists = set()
ans = 0

for _ in range(N):
    curr = input()
    if curr not in lists:
        lists.add(curr)
        ans += 1

print(ans)