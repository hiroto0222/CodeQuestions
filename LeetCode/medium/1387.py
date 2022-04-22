from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.memo = {1: 1}
    
    def check(self, x):
        if x not in self.memo:
            if x % 2 == 0:
                self.memo[x] = 1 + self.check(x // 2)
            else:
                self.memo[x] = 1 + self.check(3*x + 1)
    
        return self.memo[x]
    
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        for x in range(lo, hi + 1):
            self.check(x)
        
        ans = [(self.memo[x], x) for x in range(lo, hi + 1)]
        ans.sort()
        return ans[k - 1][1]
        

print(Solution().getKth(lo = 12, hi = 15, k = 2))
print(Solution().getKth(lo = 1, hi = 1, k = 1))
print(Solution().getKth(lo = 7, hi = 11, k = 4))
print(Solution().getKth(lo = 10, hi = 20, k = 5))
print(Solution().getKth(lo = 1, hi = 1000, k = 777))
