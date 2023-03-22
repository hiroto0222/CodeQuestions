pi = "314159265358979323846264338327"
for _ in range(int(input())):
    n = input()
    res = 0
    for i in range(len(n)):
        if n[i] == pi[i]:
            res += 1
        else:
            break

    print(res)
