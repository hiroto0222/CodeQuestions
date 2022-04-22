class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        tot_sum = 0

        for i in range(n):
            row_max = max(grid[i])
            for j in range(n):
                col_max = max(row[j] for row in grid)
                tot_sum += max(0, min(row_max, col_max) - grid[i][j])

        return tot_sum
        
    
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# grid = [[0,0,0],[0,0,0],[0,0,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))