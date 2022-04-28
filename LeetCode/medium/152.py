from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # largest product subarray
        res = max(nums)
        currMin = currMax = 1

        for num in nums:
            if num == 0:
                currMin = currMax = 1
                continue
            
            temp = currMax*num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(temp, num*currMin, num)
            res = max(res, currMax, currMin)
        
        return res


nums = [2,3,-2,4]
print(Solution().maxProduct(nums))