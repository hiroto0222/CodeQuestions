from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # brute force all combinations
        # keep updating ans list

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = [char for char in letters[digits[0]]]
        for i in range(1, len(digits)):
            temp = []
            for char in letters[digits[i]]:
                for prev in ans:
                    temp.append(prev + char)
            ans = temp.copy()
        
        return ans


digits = "23"
print(Solution().letterCombinations(digits))
