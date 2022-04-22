class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for i in range(len(min(strs, key=len))):
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                if (strs[j][i] != curr_char):
                    return ans
            ans += curr_char
        
        return ans

print(Solution().longestCommonPrefix(["flower","flow","flight"]))