from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1:
                # if value that is 0 hits boundary
                return False
            if grid[r][c] == 1:
                return True
            
            grid[r][c] = 1
            bottom = dfs(r + 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)
            top = dfs(r - 1, c)

            return bottom and right and left and top

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    closed = dfs(r, c)
                    if closed:
                        count += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print("there is a 1 at {} {}",format(r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    print("there is no other 1s")
                    
        return count
        

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(Solution().closedIsland(grid))