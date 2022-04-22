from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # dp
        # store max heights from left and right

        N = len(height)
        max_left, max_right = [0] * N, [0] * N
        curr_max = height[0]
        for i in range(N):
            if height[i] >= curr_max:
                curr_max = height[i]
            max_left[i] = curr_max
        
        curr_max = height[-1]
        for i in range(N - 1, -1, -1):
            if height[i] >= curr_max:
                curr_max = height[i]
            max_right[i] = curr_max
        
        ans = 0
        for i in range(N):
            ans += min(max_left[i], max_right[i]) - height[i]

        return ans

    def trap2Pointer(self, height: List[int]) -> int:
        if not height: return
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap2Pointer(height))