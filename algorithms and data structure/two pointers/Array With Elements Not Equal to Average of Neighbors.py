# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
from typing import List


# break the array into half
# insert item from left half and right half alternatively
# this will ensure all items from left half a surround by right item, vice versa
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        low = 0
        mid = high = len(nums) // 2 + 1

        while low < mid or high < len(nums):
            if low < mid:
                res.append(nums[low])
            if high < len(nums):
                res.append(nums[high])

            low += 1
            high += 1
        
        return res