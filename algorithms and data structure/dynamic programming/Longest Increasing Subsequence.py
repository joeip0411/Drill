from typing import List


# start from the end and moving forward
# if the current item is less than item i, we can take 1+cumulative value of item i, similar to robber
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)
