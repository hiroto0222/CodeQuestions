from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        if r * c != ROWS * COLS:
            return mat
        
        ans = [[0] * c for _ in range(r)]
        for i in range(ROWS * COLS):
            ans[i // c][i % c] = mat[i // COLS][i % COLS]

        return ans


mat = [[1,2],[3,4]]
r = 2
c = 4
print(Solution().matrixReshape(mat, r, c))