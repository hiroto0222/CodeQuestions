class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        return max(nums) if len(nums) < 3 else nums[-3]

nums = [1,2]
print(Solution().thirdMax(nums))