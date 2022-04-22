class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l, r = 0, n - 1
        ans = [0]*n

        for i in range(r, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                ans[i] = nums[r]**2
                r -= 1
            else:
                ans[i] = nums[l]**2
                l += 1

        return ans


print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))
print(Solution().sortedSquares(nums = [-7,-3,2,3,11]))
print(Solution().sortedSquares(nums = [0, 1]))
