# https://leetcode.com/problems/jump-game-ii/

from typing import List


# Time complexity = O(n^2)
def jump(nums: List[int]) -> int:
    dp = [float('inf') for _ in nums]

    dp[-1] = 0

    for i in range(len(nums)-2, -1, -1):
        for j in range(1,nums[i]+1):
            if i < len(nums):
                dp[i] = min(dp[i], 1 + dp[i+j])
            else:
                break

    return dp[0]

# Time complexity = O(n)
# BFS with tumbling window
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l = r = 0

        while r < len(nums) - 1:

            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
                
            l = r + 1
            r = farthest
            steps += 1
        
        return steps
            