# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List

# The max subarray can be in the middle (ordinary Kadane's)
# or split at both end (total - min subarray)
# only edge case is when all numbers are negative, in this case return only ordinary Kadane's (max subarray)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum1 = -float('inf')

        min_sum = float('inf')
        cur_sum2 = float('inf')

        for i in range(len(nums)):
            cur_sum1 = max(nums[i], cur_sum1 + nums[i])
            max_sum = max(cur_sum1, max_sum)

            cur_sum2 = min(nums[i], cur_sum2 + nums[i])
            min_sum = min(cur_sum2, min_sum)
        
        if max_sum < 0:
            res = max_sum
        else:
            res = max(max_sum, sum(nums) - min_sum)

        return res
