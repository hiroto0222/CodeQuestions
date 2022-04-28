from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window to check if all s1 chars are in substring of s2
        left = 0
        cnts = Counter(s1)
        for right, char in enumerate(s2):
            if char in cnts and cnts[char] > 0:
                cnts[char] -= 1
            else:
                while s2[left] != char:
                    cnts[s2[left]] += 1
                    left += 1
                left += 1
            
            if right - left + 1 == len(s1):
                return True
        
        return False

s1 = "xyz"
s2 = "xyyzx"
print(Solution().checkInclusion(s1, s2))