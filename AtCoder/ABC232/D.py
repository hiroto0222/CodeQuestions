"""
stack -> store visited paths
"""

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

dist = [[0] * W for _ in range(H)]
dist[0][0] = 1
stack = [(0, 0)]
curr_max = 1

while stack:
    curr_i, curr_j = stack.pop()
    curr_dist = dist[curr_i][curr_j]

    for i, j in [[curr_i + 1, curr_j], [curr_i, curr_j + 1]]:
        if not (i < H and j < W) or C[i][j] == "#":
            continue
        if dist[i][j] == 0:
            dist[i][j] = curr_dist + 1
            curr_max = max(curr_max, dist[i][j])
            stack.append((i, j))

print(curr_max)