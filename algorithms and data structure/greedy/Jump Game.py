# https://leetcode.com/problems/jump-game/

from typing import List

# recursive solution
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False]
        
        def jump_recur(nums):
            if res[0]:
                return
            if len(nums) <= 1:
                res[0] = True
                return

            for i in range(len(nums)-2,-1,-1):
                if i + nums[i] >= len(nums) - 1:
                    jump_recur(nums[:i+1])
        
        jump_recur(nums)
        return res[0]