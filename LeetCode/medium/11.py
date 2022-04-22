from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            ans = max(min(height[l], height[r]) * (r - l), ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return ans


height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))