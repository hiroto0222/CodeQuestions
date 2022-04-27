from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        q = deque()
        q.append((0, 0, 1))
        grid[0][0] = 1
        
        while q:
            for _ in range(len(q)):
                r, c, steps = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return steps
                
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and cc >= 0 and rr < ROWS and cc < COLS and grid[rr][cc] == 0:
                        q.append((rr, cc, steps + 1))
                        grid[rr][cc] = 1
        
        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))