N = int(input())
X = list(map(int, input().split()))
X.sort()
print(sum(X[N: 5*N - N]) / (3*N))