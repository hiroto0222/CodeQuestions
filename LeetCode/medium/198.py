from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            # [..., rob1, rob2, n, ...]
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2


nums = [1,2,3,1]
print(Solution().rob(nums))