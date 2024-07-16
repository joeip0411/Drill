# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = {n for n in nums}

        for i in range(len(nums) + 1):
            if i not in hash_set:
                return i

    # Time complexity: O(n)
    # Space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n * (n+1))//2

        for num in nums:
            total_sum -= num
        return total_sum
        