# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        max_num = max(nums)
        for i in range(len(nums)):
            if nums[i] + max_num < target:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([3, 2, 4], 6))
