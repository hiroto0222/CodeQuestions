from bisect import bisect_left

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect_left(nums, target)


print(Solution().searchInsert(nums = [1,3,5,6], target = 5))
print(Solution().searchInsert(nums = [1,3,5,6], target = 2))
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))
print(Solution().searchInsert(nums = [1,3,5,6], target = 0))
print(Solution().searchInsert(nums = [1], target = 0))
