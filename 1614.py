# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
            max_depth = max(max_depth, len(stack))

        return max_depth
