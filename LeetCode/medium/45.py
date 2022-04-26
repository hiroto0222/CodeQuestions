from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float('inf')] * N
        dp[0] = 0

        for i in range(N):
            n = nums[i]
            for j in range(1, n + 1):
                if i + j < N:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        
        return dp[-1]


nums = [2,3,1,1,4]
print(Solution().jump(nums))