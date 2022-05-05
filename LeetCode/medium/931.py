from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = ((1, 0), (1, -1), (1, 1))

        if ROWS == 1:
            return min(matrix[0])

        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS):
                curr_min = float("inf")
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if (rr in range(ROWS) and cc in range(COLS)):
                        curr_min = min(curr_min, matrix[r][c] + matrix[rr][cc])
                matrix[r][c] = curr_min
        
        return min(matrix[0])


matrix = [[-19,57]]
print(Solution().minFallingPathSum(matrix))