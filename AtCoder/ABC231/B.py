from collections import Counter


N = int(input())
votes = [input() for _ in range(N)]
print(max(votes, key=votes.count))