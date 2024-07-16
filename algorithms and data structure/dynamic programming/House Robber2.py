from typing import List

# if the first house is picked, the last house is excluded automatically, vice versa
# traverse from first house  to the second last house
# traverse from the last house to the second house
# pick the greater of the two

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)-1):
            temp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = temp
        
        ascending_dir = dp[1]

        dp = [nums[-1], max(nums[-1],nums[-2])]

        for i in range(len(nums)-3, 0, -1):
            temp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = temp

        descending_dir = dp[1]

        return max(ascending_dir, descending_dir)