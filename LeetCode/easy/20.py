class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket not in memo:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if (stack.pop() != memo[bracket]):
                    return False
        
        return len(stack) == 0

print(Solution().isValid("(}"))