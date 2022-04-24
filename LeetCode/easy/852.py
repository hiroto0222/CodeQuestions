from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search to find largest i such that arr[i] < arr[i + 1]

        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        return l


arr = [0,10,5,2]
print(Solution().peakIndexInMountainArray(arr))