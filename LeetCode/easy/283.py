class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        i, j = 0, 1
        while (i < len(nums) and j < len(nums)):
            if nums[i] == 0:
                while (j < len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        j += 1
                        i += 1
                        break
                    j += 1
            else:
                i += 1
                j += 1

nums = [0, 0, 0 ,0, 1]
Solution().moveZeroes(nums)
print(nums)