# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from typing import List


# Think in reverse, what is the longest subarray with target = sum(nums) - x
# remove immediately if cur > target, left can be greater than right at the end of the iteration
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        res = -1
        left = right = 0
        cur = 0

        for right in range(len(nums)):
            cur += nums[right]

            while cur > target and left <= right:
                cur -= nums[left]
                left += 1

            if cur == target:
                res = max(res, right - left + 1)
        
        return len(nums) - res if res != -1 else res
