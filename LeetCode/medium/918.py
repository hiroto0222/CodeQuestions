from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        tot_sum = 0
        cmax = gmax = float('-inf')
        cmin = gmin = float('inf')

        for i in range(n):
            cmax = max(nums[i], nums[i] + cmax)
            gmax = max(gmax, cmax)

            cmin = min(nums[i], nums[i] + cmin)
            gmin = min(gmin, cmin)

            tot_sum += nums[i]
        
        return max(gmax, tot_sum - gmin)


nums = nums = [5,-3,5]
print(Solution().maxSubarraySumCircular(nums))