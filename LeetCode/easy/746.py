from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP
        # mincost(n) = min(mincost(n - 2) + mincost(n - 1))
        # base case
        #  mincost(0) = cost[0]
        #  mincost(1) = cost[1]

        if not len(cost):
            return 0
        if len(cost) == 1:
            return cost[0]

        cost.append(0)
        self.memo = {0: cost[0], 1: cost[1]}

        def getMinCost(n):
            if n in self.memo:
                return self.memo[n]
            self.memo[n] = cost[n] + min(getMinCost(n - 1), getMinCost(n - 2))
            return self.memo[n]
        
        return getMinCost(len(cost) - 1)


cost = [10,15,20]
print(Solution().minCostClimbingStairs(cost))