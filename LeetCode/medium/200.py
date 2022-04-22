from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs graph
        # if grid[i][j] == "1" and not in visited:
        #   - check all neighbours that are "1" and mark them as visited (bfs)

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                curr_r, curr_c = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = curr_r + dr, curr_c + dc
                    if ((r in range(rows)) and
                       (c in range(cols)) and
                       (grid[r][c] == "1") and
                       ((r, c) not in visited)):
                            q.append((r, c))
                            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
