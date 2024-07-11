from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
                # right half is sorted
                # right half is rotated and target is at the smaller half
                # right half is roated and target is at the larger half
            elif (nums[mid] < target <= nums[right]) \
                or (target <= nums[right] < nums[mid])\
                or (nums[right] < nums[mid] < target):
                left = mid + 1
            else:
                right = mid -1
        return -1
