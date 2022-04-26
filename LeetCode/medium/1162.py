from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        if ROWS == 1 and COLS == 1:
            return -1
        
        q = deque()
        zero_elements = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print(r, c)
                    q.append((r, c))
                else:
                    zero_elements += 1
        
        visited = set()
        visited.update(q)
        count = 0

        while q and zero_elements > 0:
            print(q)
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc

                    if rr not in range(ROWS) or cc not in range(COLS):
                        continue
                    if (rr, cc) in visited:
                        continue
                    
                    # element we find is new pos of 0
                    q.append((rr, cc))
                    visited.add((rr, cc))
            
            count += 1
        
        return count - 1


grid = [[1,0,0],[0,0,0],[0,0,0]]
print(Solution().maxDistance(grid))