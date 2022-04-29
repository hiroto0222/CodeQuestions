from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        visited.add(0)
        q.append(0)
        
        while q:
            u = q.popleft()
            for v in rooms[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        
        return len(visited) == len(rooms)
        

rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))