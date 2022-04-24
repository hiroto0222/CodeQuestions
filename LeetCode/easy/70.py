class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # base cases
        #  n = 1 -> 1
        #  n = 2 -> 2
        #  n = 3 -> 3
        #  n -> (n - 2) + (n - 1)
        
        self.dp = {1: 1, 2: 2}
        
        def helper(n):
            if n in self.dp:
                return self.dp[n]
            self.dp[n] = helper(n - 2) + helper(n - 1)
            return self.dp[n]
        
        return helper(n)


n = 2
print(Solution().climbStairs(n))