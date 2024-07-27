# https://leetcode.com/problems/non-decreasing-array/

from typing import List

# When find a violation, either substitue the left item with the right item, or substitue the right item with the left item

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        swap = 1

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if swap == 1:
                    swap -= 1

                    if i > 1 and nums[i] < nums[i-2]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i-1] = nums[i] 

                else:
                    return False
        
        return True