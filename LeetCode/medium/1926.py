from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs from entrance
        
        ROWS, COLS = len(maze), len(maze[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = set()
        q = deque()
        visited.add((entrance[0], entrance[1]))
        q.append((entrance[0], entrance[1]))
        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if ([r, c] != entrance) and (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1):
                    return steps
                
                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    if (rr in range(ROWS) and
                        cc in range(COLS) and
                        (rr, cc) not in visited and
                        maze[rr][cc] == "."):
                        q.append((rr, cc))
                        visited.add((rr, cc))
                
            steps += 1
        
        return -1


maze = [[".","+"]]
entrance = [0,0]
print(Solution().nearestExit(maze, entrance))