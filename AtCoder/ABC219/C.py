X = input()
N = int(input())
S = [input() for _ in range(N)]

ans = sorted(S, key = lambda word: [X.index(c) for c in word])
for word in ans:
    print(word)