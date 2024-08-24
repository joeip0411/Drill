from typing import List


class Solution:
    # go to the side that with count that is odd
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2

            if (mid == 0) or (mid == len(nums) - 1) or (nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]):
                return nums[mid]

            left_size = mid if nums[mid] == nums[mid + 1] else mid - 1

            if left_size % 2 == 1:
                right = mid - 1
            else:
                left = mid + 1