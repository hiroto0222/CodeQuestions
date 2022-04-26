from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1: return True
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if dp[i - 1] < i:
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], nums[i] + i)
            print(dp)
        
        return dp[-1] >= n - 1

    def canJumpGreedy(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


nums = [2,3,1,1,4]
print(Solution().canJumpGreedy(nums))