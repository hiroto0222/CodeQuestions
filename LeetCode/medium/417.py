from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()  # visited for each ocean case
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # every position in first row for pacfic
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # every position in last row for atlantic
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # every position in first col for pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # every position last col for atlantic
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(heights))