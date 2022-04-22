from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_combo, curr_sum):
            if curr_sum == target:
                res.append(curr_combo.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            curr_combo.append(candidates[i])
            dfs(i, curr_combo, curr_sum + candidates[i])
            curr_combo.pop()
            dfs(i + 1, curr_combo, curr_sum)
        
        dfs(0, [], 0)
        return res


candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))