class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        currMax = 0
        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            else:
                currMax = max(currMax, prices[i] - currMin)
        
        return currMax