from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # T/S: O(mn)
        start_pixel = image[sr][sc]
        
        # there is no work to be done
        if start_pixel == newColor:
            return image
        
        m, n = len(image), len(image[0])
        queue = deque([(sr, sc)])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        # in bounds and same pixel as our starting pixel
        def is_valid(r, c):
            return r in range(m) and c in range(n) and start_pixel == image[r][c]
        
        while queue:
            r, c = queue.popleft()
            image[r][c] = newColor
            
            # try all 4 directions (down, right, up, left)
            for dr, dc in dirs:
                if is_valid(r + dr, c + dc):
                    queue.append((r + dr, c + dc))
                    
        return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 1
print(Solution().floodFill(image, sr, sc, newColor))