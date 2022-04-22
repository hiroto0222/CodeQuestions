from bisect import bisect_left

class Solution(object):
    def search(self, nums, target):
        index = bisect_left(nums, target)
        return index if (index != len(nums) and nums[index] == target) else -1

print(Solution().search(nums = [-1,0,3,5,9,12], target = 9))
print(Solution().search(nums = [-1,0,3,5,9,12], target = 2))
