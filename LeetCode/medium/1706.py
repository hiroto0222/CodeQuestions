from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0]) 
        ans = [i for i in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                curr_col = ans[col]
                if curr_col == -1:
                    continue
                
                direction = grid[row][curr_col]
                adj = curr_col + direction
                if adj >= COLS or adj < 0 or grid[row][adj] != direction:
                    ans[col] = -1
                else:
                    ans[col] = adj

        return ans


grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
grid = [[1, -1]]
print(Solution().findBall(grid))