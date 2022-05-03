from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # fresh orange count
        # keep decrementing fresh orange cnt till 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = deque()
        visited = set()
        fresh_cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_cnt += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        if fresh_cnt == 0:
            return 0
        
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    fresh_cnt -= 1
                
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if (rr in range(ROWS) and
                        cc in range(COLS) and
                        (rr, cc) not in visited and
                        grid[rr][cc] == 1):
                        q.append((rr, cc))
                        visited.add((rr, cc))
                
            if not q:
                break
            steps += 1
        
        return -1 if fresh_cnt > 0 else steps


grid = [[2,2],[1,1],[0,0],[2,0]]
print(Solution().orangesRotting(grid))