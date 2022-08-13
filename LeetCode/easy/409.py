from collections import defaultdict


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = defaultdict(int)
        for c in s:
            cnts[c] += 1
        
        extra = False
        ans = 0
        for c in list(cnts.keys()):
            if cnts[c] % 2 != 0:
                cnts[c] -= 1
                ans += cnts[c]
                extra = True
            else:
                ans += cnts[c]
        
        return ans + 1 if extra else ans


s = "abccccdd"
print(Solution().longestPalindrome(s))