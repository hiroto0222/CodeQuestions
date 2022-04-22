class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, longest = len(s), ""
        dp_table = [[False for i in range(n)] for j in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp_table[i][j] = True
                elif j-i == 1:
                    dp_table[i][j] = s[i] == s[j]
                if dp_table[i][j]: # If palindromic substring, update longest 
                    longest = s[i:j+1] if j+1-i > len(longest) else longest
        
        for i in reversed(range(n)):
            for j in range(i+2, n):
                if s[i] == s[j] and dp_table[i+1][j-1]:
                    dp_table[i][j] = True
                if dp_table[i][j]: # If palindromic substring, update longest 
                    longest = s[i:j+1] if j+1-i > len(longest) else longest

        return longest


test = ["babad", "cbbd", "a", "ac"]

for s in test:
    print(Solution().longestPalindrome(s))
