class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        memo = nums[:]

        for i in range(n):
            nums[i] = memo[(i - k) % n]
        
        return nums

print(Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(Solution().rotate(nums = [-1,-100,3,99], k = 2))
