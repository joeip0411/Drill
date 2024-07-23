# https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.cur_sum = 0
        self.prefix_sum = []

        for n in nums:
            self.cur_sum += n
            self.prefix_sum.append(self.cur_sum)


    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0

        return right_sum - left_sum
