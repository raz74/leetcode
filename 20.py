# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            elif char in ")]}":
                if len(stack) == 0:
                    return False
                if stack.pop() != mapping[char]:
                    return False

        if len(stack) != 0:
            return False

        return True



print(Solution().isValid("((("))
