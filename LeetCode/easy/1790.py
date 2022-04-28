class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 2
        i = 0
        swap = []
        while i < len(s1):
            if s1[i] != s2[i]:
                cnt -= 1
                swap.append(i)
            i += 1
                
        if not swap:
            return True
        if len(swap) < 2 or len(swap) > 2:
            return False
        return s1[swap[0]] == s2[swap[1]] and s1[swap[1]] == s2[swap[0]]