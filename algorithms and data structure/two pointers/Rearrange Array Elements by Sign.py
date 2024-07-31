# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List


# two pointers to look for pos and neg numbers
# Time complexity = O(n)
# Space complexity = O(n) for mainting the output array
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        res = []

        while len(res) < len(nums):
            while pos < len(nums) and nums[pos] < 0:
                pos += 1
            
            res.append(nums[pos])
            pos += 1

            while neg < len(nums) and nums[neg] > 0:
                neg += 1
            
            res.append(nums[neg])
            neg += 1
        
        return res
    

# pre building the result array, keep track target index for pos and negative
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2
        
        return res