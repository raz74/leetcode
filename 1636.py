from collections import Counter
# https://leetcode.com/problems/sort-array-by-increasing-frequency/


class Solution:
    def frequencySort(self, nums: [int]) -> [int]:
        frequency = Counter(nums)
        return sorted(nums, key=lambda a: (frequency[a], -a))
