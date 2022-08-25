from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(min(ROWS, COLS) - 1):
            for col in range(i, COLS - i - 1):
                print(matrix[i][col])
            
            for row in range(i, ROWS - i - 1):
                print(matrix[row][COLS - i - 1])
            
            for col in range(COLS - i - 1, i, -1):
                print(matrix[ROWS - i - 1][col])
            
            for row in range(ROWS - i - 1, i, -1):
                print(matrix[row][i])


matrix = [[1, 2]]
print(Solution().spiralOrder(matrix))