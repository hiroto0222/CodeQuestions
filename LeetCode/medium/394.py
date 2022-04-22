class Solution:
    def decodeString(self, s: str) -> str:
        # num stack
        # keep track of curr string
        # pop num after ]

        stack = []
        curr_multiplier = 0
        curr_str = ""
        for char in s:
            if char.isalpha():
                curr_str += char
            elif char.isdigit():
                i = int(char)
                curr_multiplier *= 10
                curr_multiplier += i
            elif char == "[":
                stack.append((curr_str, curr_multiplier))
                curr_multiplier = 0
                curr_str = ""
            elif char == "]":
                prev_str, mult = stack.pop()
                curr_str = prev_str + curr_str * mult

        return curr_str
        
s = "3[a2[c]]"
print(Solution().decodeString(s))