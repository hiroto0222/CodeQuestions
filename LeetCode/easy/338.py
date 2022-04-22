from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        last = -1
        for i in range(1, n + 1):
            is_2_power = i & (i - 1) == 0
            if is_2_power:
                last = i
            ans.append(1 + (0 if is_2_power else ans[i - last]))
        
        return ans


n = 5
print(Solution().countBits(n))