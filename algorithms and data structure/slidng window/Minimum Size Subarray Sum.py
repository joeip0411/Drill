# https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_length = float('inf')
        max_sum = 0

        for R in range(len(nums)):
            max_sum += nums[R]

            while max_sum >= target:
                min_length = min(min_length, R - L + 1)
                max_sum -= nums[L]
                L += 1
        
        res = 0 if min_length == float('inf') else min_length

        return res
