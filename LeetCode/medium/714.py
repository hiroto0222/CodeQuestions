from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        ans = 0
        minimum = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        
        return ans


prices = [1,3,2,8,4,9]
fee = 2
print(Solution().maxProfit(prices, fee))