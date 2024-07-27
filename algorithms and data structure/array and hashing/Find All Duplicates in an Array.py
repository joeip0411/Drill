# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from typing import List


# mark a number visited in the input array by changing the sign
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            idx_visit = abs(nums[i]) - 1

            if nums[idx_visit] < 0:
                res.append(abs(nums[i]))
            
            nums[idx_visit] *= -1
        
        return res