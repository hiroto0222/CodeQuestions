from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnts = Counter(nums)
        return [i[0] for i in cnts.items() if i[1] == 2]

print(Solution().findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(Solution().findDuplicates(nums = [1,1,2]))
print(Solution().findDuplicates(nums = [1]))
