import math


class SolutionNotOptimal:
    def isPalindrome(self, x: int) -> bool:
        converted_num = str(x)
        if converted_num == converted_num[::-1]:
            return True
        else:
            return False

# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        while x > 0:
            digits = int(math.log10(x)) + 1
            if x % 10 != x // 10 ** (digits - 1):
                return False
            x = x % 10 ** (digits - 1)
            x = x // 10
        return True


print(Solution().isPalindrome(1000021))
