# https://leetcode.com/problems/find-pivot-index/description/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cur_sum = 0
        prefix = []

        for n in nums:
            cur_sum += n
            prefix.append(cur_sum)
        
        for i in range(len(nums)):
            left_sum = prefix[i-1] if i > 0 else 0
            right_sum = prefix[-1] - prefix[i]

            if left_sum == right_sum:
                return i
        
        return -1