class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointers
        
        if len(s) == 0:
            return 0
        
        l = r = 0
        currSeen = set()
        ans = curr = 0
        while r < len(s):
            print(l, r, currSeen)
            if s[r] not in currSeen:
                currSeen.add(s[r])
                curr += 1
                r += 1
            else:
                ans = max(ans, curr)
                currSeen.remove(s[l])
                curr -= 1
                l += 1
                
        ans = max(ans, curr)
        return ans


s = "aab"
print(Solution().lengthOfLongestSubstring(s))