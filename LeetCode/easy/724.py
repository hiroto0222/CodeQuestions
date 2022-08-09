class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total sum and subtract

        tot_sum = sum(nums)
        left = 0
        for i, mid in enumerate(nums):
            if left == (tot_sum - left - mid):
                return i
            left += mid

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
