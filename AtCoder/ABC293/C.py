H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0

def dfs(i, j, seen):
    global ans
    
    if i == H - 1 and j == W - 1:
        if len(set(seen)) == len(seen):
            ans += 1
        return
    
    if i + 1 < H:
        seen.append(A[i + 1][j])
        dfs(i + 1, j, seen)
        seen.pop()
    
    if j + 1 < W:
        seen.append(A[i][j + 1])
        dfs(i, j + 1, seen)
        seen.pop()

dfs(0, 0, [A[0][0]])
print(ans)