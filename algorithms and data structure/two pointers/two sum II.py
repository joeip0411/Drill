# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/281669286/

# the array is sorted, this is the main property we have to leverage

# the solution can only used constant extra space, that means we cannot use a dict to track the items

from typing import List



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1