# https://leetcode.com/problems/binary-subarrays-with-sum/
from typing import List


# Find number of subarray <= goal and number of subarray <= goal - 1, take the difference betweeb the two
# We have to do this because there are 0s in the array
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def num_subarray(nums, x):
            if x < 0:
                return 0

            res = 0 
            left = 0
            cur = 0

            for right in range(len(nums)):
                cur += nums[right]

                while cur > x and left <= right:
                    cur -= nums[left]
                    left += 1
                
                res += right - left + 1

            return res
        
        return num_subarray(nums, goal) - num_subarray(nums, goal - 1)

# Using prefix sum and hash map to keep track of frequency of subarray with certain prefix sum
# Time complexity = O(n)
# Space complexity = O(n)
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        prefix = 0
        res = 0

        for n in nums:
            prefix += n

            if prefix - goal in hash_map:
                res += hash_map[prefix - goal]

            hash_map[prefix] += 1
        
        return res