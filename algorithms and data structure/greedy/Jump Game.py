# https://leetcode.com/problems/jump-game/

from typing import List

# the brute force solution is O(n^n), i.e. The array is sorted in descending order

# Dynamic programming
# The last item can always reach it self
# If the current item has enough steps to reach a True node, than it is also True
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(1,nums[i]+1):
                if dp[i+j]:
                    dp[i] = True
                    break
        
        return dp[0]

# Further optimisation, store the target, 
# see if the current node can pass the target
# if true, update the target to the current node
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return target == 0