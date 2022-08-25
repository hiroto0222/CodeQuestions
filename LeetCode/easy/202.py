class Solution:
    def isHappy(self, n: int) -> bool:
        # sum of squares of digits
        # repeat till == 1 or loops endlessly (use set to keep track of seen)
        # if == 1 -> happy

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


n = 19
print(Solution().isHappy(n))