from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red -> white -> blue
        # 0 -> 1 -> 2
        
        count = {0: 0, 1: 0, 2: 0}
        for val in nums:
            count[val] += 1
        
        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0], count[0] + count[1]):
            nums[i] = 1
        for i in range(count[0] + count[1], len(nums)):
            nums[i] = 2
    
    def sortColorsPartition(self, nums):
        l, r = 0, len(nums) - 1
        i = 0
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1


nums = [2,0,2,1,1,0]
print(Solution().sortColorsPartition(nums))
print(nums)