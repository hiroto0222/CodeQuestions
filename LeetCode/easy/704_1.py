class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if (len(nums) == 1):
            return 0

        while (left < right):
            mid = (left + right) // 2
            print(mid)
            if (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else: return mid

        return -1


nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))

nums = [5]
target = 5
print(Solution().search(nums, target))