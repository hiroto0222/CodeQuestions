from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window

        l = 0
        prod = 1
        res = 0

        for r in range(len(nums)):
            prod *= nums[r]

            if prod >= k:
                while prod >= k and l <= r:
                    prod //= nums[l]
                    l += 1
            
            res += (r - l + 1)
        
        return res


nums = [1, 1, 1, 1]
k = 2
print(Solution().numSubarrayProductLessThanK(nums, k))