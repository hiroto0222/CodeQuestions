class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) == 0):
            return True
        if (len(t) == 0):
            return False

        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if (j >= len(s)):
                return True
        return j == len(s)


print(Solution().isSubsequence(s="abc", t="ahbgdc"))
print(Solution().isSubsequence(s="as", t=""))
