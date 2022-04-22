class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0): return 0
        if (x == 1): return 1
        left, right = 0, x
        while (left < right):
            mid = (left + right) // 2
            print("curr mid {}".format(mid))
            if (mid * mid < x):
                left = mid + 1
            elif (mid * mid == x):
                return mid
            else:
                right = mid
        
        return left - 1

print(Solution().mySqrt())