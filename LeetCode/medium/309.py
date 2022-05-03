from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: Buying or Selling
        # if buy -> i + 1
        # if sell -> i + 2

        dp = {}  # key = (i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # max profit associated with each decision
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, buying=True) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)


prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))