from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])

        print(dp)
        return dp[0][0]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))