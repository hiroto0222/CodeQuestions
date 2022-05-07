from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # obstacles -> "#"
        # bottom row first

        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "#"
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if i == ROWS - 1 and j == COLS - 1:
                    obstacleGrid[i][j] = 1
                    continue
                
                if obstacleGrid[i][j] == "#": continue

                down, right = 0, 0
                if i != ROWS - 1 and obstacleGrid[i + 1][j] != "#":
                    down = obstacleGrid[i + 1][j]
                if j != COLS - 1 and obstacleGrid[i][j + 1] != "#":
                    right = obstacleGrid[i][j + 1]
                
                obstacleGrid[i][j] = down + right
        
        return obstacleGrid[0][0]
    
    def uniquePathsWithObstaclesRecursive(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r > ROWS - 1 or c > COLS - 1 or obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                dp[r][c] = 1
                return 1
            
            if dp[r][c] != -1:
                return dp[r][c]

            dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[r][c]

        return dfs(0, 0)


obstacleGrid = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
print(Solution().uniquePathsWithObstaclesRecursive(obstacleGrid))