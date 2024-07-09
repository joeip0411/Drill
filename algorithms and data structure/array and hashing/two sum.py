# https://leetcode.com/problems/two-sum/description/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}

        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [num_map[target - nums[i]], i]
            else:
                num_map[nums[i]] = i