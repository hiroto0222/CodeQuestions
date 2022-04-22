"""
if ball k is placed k consecutive times, then all k balls dissapear
for each i, output how many balls

stack
"""

N = int(input())
a = list(map(int, input().split()))

stack = []
cnt = 0
for i in range(N):
    if not stack:
        stack.append([a[i], 1])
        cnt += 1
    else:
        if stack[-1][0] == a[i]:
            stack[-1][1] += 1
            cnt += 1

            if (stack[-1][0] == stack[-1][1]):
                cnt -= stack.pop()[1]
        else:
            stack.append([a[i], 1])
            cnt += 1
    print(cnt)
    