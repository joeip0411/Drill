# https://leetcode.com/problems/maximum-product-subarray/

from typing import List



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = 1
        res = -float('inf')

        for num in nums:
            if nums == 0:
                cur_min = cur_max = 1
                continue

            temp = cur_max * num
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)

            res = max(res, cur_max)
        
        return res