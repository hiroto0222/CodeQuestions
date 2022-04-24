from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def bfs(r, c):
            DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            curr_area = 0
                
            while q:
                curr_area += 1
                row, col = q.popleft()
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
            
            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_area = bfs(r, c)
                    max_area = max(curr_area, max_area)

        return max_area


grid = [[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))