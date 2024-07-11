from typing import List


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        # if prev and next item greater than self, than it must be the min
        if nums[mid-1] > nums[mid] and nums[(mid + 1) % len(nums)] > nums[mid]:
            return nums[mid]
        # if the right most item is less than self, than the min must on the right half
        elif nums[right] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1