# https://leetcode.com/problems/find-peak-element/
from typing import List


# always go to the side where the neighbour is larger than the current item
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        left = 0 
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2

            if (mid == 0 and nums[mid + 1] < nums[mid]) \
                or (mid == len(nums) - 1 and nums[mid - 1] < nums[mid]) \
                or (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                return mid
            elif (nums[mid + 1] > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
