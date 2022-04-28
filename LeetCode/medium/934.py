from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def invalid(r, c):
            return r < 0 or c < 0 or r == ROWS or c == COLS
        
        def dfs(r, c):
            if invalid(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visited)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in DIRS:
                        rr, cc = r + dr, c + dc
                        if invalid(rr, cc) or (rr, cc) in visited:
                            continue
                        if grid[rr][cc] == 1:  # visited other island
                            return res
                        q.append((rr, cc))
                        visited.add((rr, cc))
                
                res += 1

        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)  # fills in visited hashset with 1st island found
                    return bfs()


grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(grid))