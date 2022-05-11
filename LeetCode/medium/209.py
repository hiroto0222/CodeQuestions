from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_min = float('inf')
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= target:
                curr_min = min(curr_min, (r - l + 1))
                while curr_sum >= target:
                    curr_sum -= nums[l]
                    l += 1
                    if curr_sum >= target:
                        curr_min = min(curr_min, (r - l + 1))
        
        return -1 if curr_min == float('inf') else curr_min


target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))