from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        l = 0
        cnts, tot_cnt = Counter(p), len(p)
        ans = []

        for r in range(len(s)):
            if s[r] not in cnts:
                cnts = Counter(p)
                tot_cnt = len(p)
                l = r + 1
                continue

            if s[r] in cnts:
                if cnts[s[r]] > 0:
                    cnts[s[r]] -= 1
                    tot_cnt -= 1

                    if tot_cnt == 0:
                        ans.append(l)
                        cnts[s[l]] += 1
                        tot_cnt += 1
                        l += 1
                else:
                    while s[l] != s[r]:
                        cnts[s[l]] += 1
                        tot_cnt += 1
                        l += 1
                    l += 1

        return ans


s = "cbababababca"
p = "abc"
print(Solution().findAnagrams(s, p))