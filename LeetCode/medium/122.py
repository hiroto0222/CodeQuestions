from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        res = 0
        lowest = prices[0]
        for i in range(1, len(prices) - 1):
            if prices[i + 1] <= prices[i]:
                res += max(0, prices[i] - lowest)
                lowest = prices[i + 1]
            
            elif prices[i] < lowest:
                lowest = prices[i]

        return max(res, res + prices[-1] - lowest)


prices = [6,1,3,2,4,7]
print(Solution().maxProfit(prices))