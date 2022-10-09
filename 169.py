# https://leetcode.com/problems/majority-element/submissions/

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        _dict = {}
        for i in nums:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1

        return max(_dict, key=_dict.get)


