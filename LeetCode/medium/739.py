from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            if not stack:
                stack.append([i, val])
            else:
                while stack and stack[-1][1] < val:
                    curr_i = stack.pop()[0]
                    ans[curr_i] = i - curr_i

                stack.append([i, val])

        return ans

# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))