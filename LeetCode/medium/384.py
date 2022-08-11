import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def shuffle(self):
        """
        :rtype: List[int]
        """
        # Knuth shuffle
        randNums = list(self.nums)
        for i in range(len(self.nums)):
            randIdx = i + random.randint(len(self.nums) - i - 1)
            self.swap(randNums, i, randIdx)
        
        return randNums
