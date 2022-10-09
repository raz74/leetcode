# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        _dict = {}
        for num in nums:
            _dict[num] = 0

        x = 0
        for i in range(len(nums)):
            candide1 = nums[i] + k
            candide2 = nums[i] - k
            if candide1 in _dict or candide2 in _dict:
                x += 1
        return x


print(Solution().countKDifference([1, 2, 2, 1], 1))
