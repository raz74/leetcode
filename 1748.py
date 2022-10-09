# https://leetcode.com/problems/sum-of-unique-elements/submissions/

class Solution:
    def sumOfUnique(self, nums: [int]) -> int:
        _dict = {}
        sum1 = 0
        for i in nums:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1

        for key, val in _dict.items():
            if val == 1:
                sum1 += key
        return sum1`

