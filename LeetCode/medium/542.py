from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS for shortest path for each cell
    
        ROWS, COLS = len(mat), len(mat[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = "#"
        
        for r, c in q:
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if (rr in range(ROWS) and cc in range(COLS) and mat[rr][cc] == "#"):
                    mat[rr][cc] = mat[r][c] + 1
                    q.append((rr, cc))
        
        return mat


mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat))