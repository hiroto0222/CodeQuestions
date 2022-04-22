from string import ascii_lowercase

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    letters = ascii_lowercase

    curr = ''
    ans = []
    for i in range(n):
        if a[i] == 0:
            curr = letters[i % 26]
            ans.append(curr)
        elif a[i] != 0 and i == 0:
            curr = letters[i % 26] * a[i]
            ans.append(curr)
        elif a[i] > a[i - 1]:
            curr += letters[i % 26] * (a[i] - a[i - 1])
            ans.append(curr)
        else:
            curr = curr[:a[i]]
            ans.append(curr)
        
        if i == n - 2:
            if a[i] == 0:
                curr = letters[(i + 2) % 26]
                ans.append(letters[(i + 2) % 26])
            else:
                ans.append(curr)

    for i in ans:
        print(i)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    ans = ['a' * (mx + 1)] * (n + 1)

    for i, x in enumerate(a):
        temp = 'a' if ans[i][x] == 'b' else 'b'
        ans[i + 1] = ans[i][:x] + temp + ans[i][x + 1:]
    
    print('\n'.join(ans))