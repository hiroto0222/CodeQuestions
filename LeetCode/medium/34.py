from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        start = binarySearch(nums, target)
        end = binarySearch(nums, target + 1) - 1

        if start < len(nums) and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]


nums = []
target = 0
print(Solution().searchRange(nums, target))