class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ans = 0
        len_s, len_t = len(s), len(t)

        for i in range(len_s):
            for j in range(len_t):
                x, y = i, j
                cnt = 0

                while x < len_s and y < len_t:
                    if s[x] != t[y]:
                        cnt += 1

                    if cnt == 1:
                        ans += 1
                    
                    if cnt == 2:
                        break

                    x += 1
                    y += 1
    
        return ans


print(Solution().countSubstrings(s = "aba", t = "baba"))
print(Solution().countSubstrings(s = "ab", t = "bb"))
