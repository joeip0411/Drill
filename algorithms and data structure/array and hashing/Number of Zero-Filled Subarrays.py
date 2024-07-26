# https://leetcode.com/problems/number-of-zero-filled-subarrays/
from typing import List


class Solution:
    # sliding window to count number of consecutive 0 , 
    # 1 + 2 + 3 + 4... -> k * (k+1) / 2

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0

        while left < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
                continue
            
            while right < len(nums) and nums[right] == 0:
                right += 1
            
            count = right - left
            comb = count * (count + 1) // 2
            res += comb

            left = right
            

        return res
            