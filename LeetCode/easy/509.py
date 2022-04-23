class Solution:
    def fib(self, n: int) -> int:
        self.memo = {0: 0, 1: 1, 2: 1}
        
        def getFib(n):
            if n in self.memo:
                return self.memo[n]
            self.memo[n] = getFib(n - 1) + getFib(n - 2)
            return self.memo[n]
        
        return getFib(n)


n = 4
print(Solution().fib(n))