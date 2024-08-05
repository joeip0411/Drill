# https://leetcode.com/problems/subarray-product-less-than-k/
from typing import List


# add window size to result if product < k, neutral number is 1
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        cur = 1

        for right in range(len(nums)):
            cur *= nums[right]

            while cur >= k and left <= right:
                cur /= nums[left]
                left += 1

            if cur < k:
                res += right - left + 1
        
        return res