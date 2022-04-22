import math

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        currSum, maxSum = 0, -math.inf
        for i in range(n):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if (currSum < 0): currSum = 0
        
        return maxSum


print(Solution().maxSubArray([-1]))