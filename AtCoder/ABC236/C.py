N, M = map(int, input().split())
S = list(input().split())
T = set(list(input().split()))

for station in S:
    if station in T:
        print("Yes")
    else:
        print("No")
