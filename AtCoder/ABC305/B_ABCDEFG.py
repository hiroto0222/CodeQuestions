p, q = input().split()
dist = [3, 1, 4, 1, 5, 9]

if p > q:
    p, q = q, p

s, e = ord(p) - ord("A"), ord(q) - ord("A") - 1
print(sum(dist[s : e + 1]))
