from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]

        for c in s:
            tmp = []
            if c.isalpha():
                for x in ans:
                    tmp.append(x + c.lower())
                    tmp.append(x + c.upper())
            else:
                for x in ans:
                    tmp.append(x + c)
            ans = tmp
        
        return ans
    
    def letterCasePermutationRecursive(self, s: str) -> List[str]:

        def backtrack(string, word):
            if not string:
                res.append(word)
                return
            
            if string[0].isalpha():
                backtrack(string[1:], word + string[0].upper())
                backtrack(string[1:], word + string[0].lower())
            else:
                backtrack(string[1:], word + string[0])
        
        res = []
        backtrack(s, "")
        return res


s = "a1b2"
print(Solution().letterCasePermutationRecursive(s))