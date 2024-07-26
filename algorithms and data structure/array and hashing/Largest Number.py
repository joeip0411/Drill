# https://leetcode.com/problems/largest-number/description/

from functools import cmp_to_key
from typing import List



# comparing two integers and determine which one should go first
# "9", "34" -> "934", "349"
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if sum(nums) == 0:
            return '0'

        nums = [str(i) for i in nums]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(compare))

        res = ''.join(nums)

        return res