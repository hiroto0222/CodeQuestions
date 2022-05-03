from typing import List


class Solution:
    # DFS Approach
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = set()
        
        def dfs(start):
            visited.add(start)
            for v in range(n):
                if isConnected[start][v] and v not in visited:
                    dfs(v)
        
        for start in range(n):
            if start not in visited:
                provinces += 1
                dfs(start)
        
        return provinces

    # Union Find Approach
    

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))