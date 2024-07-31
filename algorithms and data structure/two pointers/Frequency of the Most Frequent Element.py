# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
from typing import List


class Solution:
    # sort the array, so that difference between adjacent items is minimised
    # keep track of total and determine if window is valid
    # if not decrease window size by shifting left pointer one spot to the right

    # Time complexity = O(n) because the left / right pointer is shifted one spot to the right in each iteration
    # Space complexity = O(1)
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = left + 1
        res = 1
        total = nums[left]

        while right < len(nums):
            if nums[right] * (right - left) - total <= k:
                res = max(res, right - left + 1)
                total += nums[right]
                right += 1
            else:
                total -= nums[left]
                left = left + 1
                
        return res