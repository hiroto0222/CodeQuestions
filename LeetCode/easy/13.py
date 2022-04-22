class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans, prev = 0, 0
        for char in reversed(s):
            curr = memo[char]
            if (curr < prev):
                ans -= curr
            else: ans += curr
            prev = curr

        return ans

print(Solution().romanToInt("MCMXCIV"))