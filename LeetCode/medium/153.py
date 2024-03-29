from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find pos where nums[i] <= nums[i + 1]
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        if nums[r] > nums[l]:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


nums = [3,4,5,1,2]
print(Solution().findMin(nums))