class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dfs(row_idx, col_idx, cache={}):
            if row_idx >= len(triangle):
                return 0
            
            if col_idx >= len(triangle[row_idx]) or col_idx < 0:
                return float("inf")
            
            if (row_idx, col_idx) in cache:
                return cache[(row_idx, col_idx)]
                  
            bottom_adj = triangle[row_idx][col_idx] + dfs(row_idx+1, col_idx)
            bottom_right_adj = triangle[row_idx][col_idx] + dfs(row_idx+1, col_idx+1)
                
            cache[(row_idx, col_idx)] = min(bottom_adj, bottom_right_adj)
            
            return cache[(row_idx, col_idx)]

        return dfs(0, 0)