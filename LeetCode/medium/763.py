from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnts = Counter(s)
        ans = []
        l = 0
        curr_chars = set()

        for r in range(len(s)):
            cnts[s[r]] -= 1
            curr_chars.add(s[r])
            
            check = len(curr_chars)
            for char in curr_chars:
                if cnts[char] == 0:
                    check -= 1

            if check == 0:
                ans.append(r - l + 1)
                curr_chars = set()
                l = r + 1
        
        return ans

s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))
