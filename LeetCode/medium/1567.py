from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        left = right = 0
        negatives = 0

        while left < len(nums):
            while right < len(nums) and nums[right] != 0:
                if nums[right] < 0:
                    negatives += 1
                right += 1
                if negatives % 2 == 0:
                    ans = max(ans, right - left)
            
            while left < right:
                if nums[left] < 0:
                    negatives -= 1
                left += 1
                if negatives % 2 == 0:
                    ans = max(ans, right - left)
            
            right += 1
            left = right
    
        return ans


nums = [1,-2,-3,4]
print(Solution().getMaxLen(nums))