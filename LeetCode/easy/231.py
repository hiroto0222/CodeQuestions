class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 0 else bin(n)[2:].count('1') == 1


n = 3
print(Solution().isPowerOfTwo(n))