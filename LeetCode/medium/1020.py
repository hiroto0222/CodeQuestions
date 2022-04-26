from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c) -> bool:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if grid[r][c] == 0:
                return True
            else:
                self.curr_cnt += 1

            grid[r][c] = 0
            top = dfs(r - 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            bottom = dfs(r + 1, c)

            return top and left and right and bottom

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.curr_cnt = 0
                    closed = dfs(r, c)
                    if closed:
                        count += self.curr_cnt
        
        return count



grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(Solution().numEnclaves(grid))