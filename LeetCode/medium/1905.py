from collections import deque
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        count = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid2[r][c] == 0 or (r, c) in visited:
                return True

            visited.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False
            
            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1

        return count

    def countSubIslandsBFS(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        count = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            isIsland = True
            
            while q:
                row, col = q.popleft()
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid2[r][c] == 1):
                        if grid1[r][c] == 0:
                            isIsland = False
                        q.append((r, c))
                        visited.add((r, c))
            
            return isIsland

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and grid1[r][c] == 1 and (r, c) not in visited:
                    isSubisland = bfs(r, c)
                    if isSubisland:
                        count += 1

        return count


grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(Solution().countSubIslandsBFS(grid1, grid2))