# https://leetcode.com/problems/132-pattern/
from typing import List


# monotonically decreasing stack
# keep popping from stack when the current item is greater than the top of the stack
# also keep track of the min item to the left, this is to maximise the gap between 1 and 3
# when new item falls between 1 and 3, return True
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = nums[0]

        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True
            
            stack.append([nums[i], cur_min])
            cur_min = min(cur_min, nums[i])
        
        return False