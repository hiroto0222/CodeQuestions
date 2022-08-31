from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnts = Counter(words)
        res, hasOdd = 0, False

        for word in cnts.keys():
            if word == word[::-1]:
                if cnts[word] % 2 == 1:
                    hasOdd = True
                res += 2 * (cnts[word] if cnts[word] % 2 == 0 else cnts[word] - 1)
            else:
                res += min(cnts[word], cnts[word[::-1]]) * 2
        
        return res + (2 if hasOdd else 0)

words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
print(Solution().longestPalindrome(words))