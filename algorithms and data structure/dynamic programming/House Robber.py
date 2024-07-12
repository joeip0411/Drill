# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp
        
        return dp[1]