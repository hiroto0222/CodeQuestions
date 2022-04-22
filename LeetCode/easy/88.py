class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1, -1, -1):
            
            if (m > 0 and n > 0):
                if (nums1[m - 1] < nums2[n - 1]):
                    nums1[i] = nums2[n - 1]
                    n -= 1
                else:
                    nums1[i] = nums1[m - 1]
                    m -= 1
            
            elif (n > 0 and m == 0):
                nums1[i] = nums2[n - 1]
                n -= 1
            
            elif (m > 0 and n == 0):
                continue
            
            print(True ^ True)


nums1 = [1,2,4,5,6,0]
print(Solution().merge(nums1, 5, [3], 1))
print(nums1)