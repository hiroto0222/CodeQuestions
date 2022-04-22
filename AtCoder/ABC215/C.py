from itertools import permutations

S, K = input().split()
K = int(K)
arr = sorted(list(set(list(permutations(S, len(S))))))
ans = arr[K - 1]
print("".join(list(ans)))