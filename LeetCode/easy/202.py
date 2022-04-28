class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:            
            curr = 0
            while n > 0:
                curr += (n % 10) ** 2
                n //= 10
            
            if curr in seen:
                return False
            
            if curr == 1:
                return True
            
            seen.add(curr)
            n = curr


n = 1
print(Solution().isHappy(n))