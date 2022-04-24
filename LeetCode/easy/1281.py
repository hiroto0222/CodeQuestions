class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tot_prod, tot_sum = 1, 0
        while n > 0:
            curr = n % 10
            tot_prod *= curr
            tot_sum += curr
            n //= 10
        
        return tot_prod - tot_sum


n = 4401
print(Solution().subtractProductAndSum(n))