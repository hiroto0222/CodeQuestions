from typing import List


class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_partition = []
        dp = [[False] * len(s)] * len(s)

        def dfs(start):
            if start >= len(s):
                res.append(curr_partition.copy())
                return
            
            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    curr_partition.append(s[start:end + 1])
                    dfs(end + 1)
                    curr_partition.pop()
        
        dfs(0)
        return res


s = "aab"
print(Solution().partition(s))