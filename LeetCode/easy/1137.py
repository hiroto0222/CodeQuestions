class Solution:
    def tribonacci(self, n: int) -> int:
        # T(0) -> 0
        # T(1) -> 1
        # T(2) -> 1
        # T(n + 3) -> T(n) + T(n + 1) + T(n + 2)

        self.memo = {0: 0, 1: 1, 2: 1}

        def helper(n):
            if n in self.memo:
                return self.memo[n]
            self.memo[n] = helper(n - 3) + helper(n - 2) + helper(n - 1)
            return self.memo[n]

        return helper(n)  


n = 25
print(Solution().tribonacci(n))