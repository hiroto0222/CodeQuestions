from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # dp
        counts = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            currEarn = nums[i] * counts[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(currEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = currEarn + earn2
                earn1 = temp
        
        return earn2


nums = [2,2,3,3,3,4]
print(Solution().deleteAndEarn(nums))