# https://leetcode.com/problems/contiguous-array/

from typing import List

# at each position calculate difference between numbers of 0 and 1
# e.g. if diff is +2, we want to see if we can remove a prefix with 2 extra 1s
# This can be accomplish by also storing the diff in a hash map along with the index, we never update a key because we want the index to be smallest, i.e. removing the shortest prefix.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        hash_map = {}
        max_length = 0

        for idx, val in enumerate(nums):
            diff += 1 if val == 1 else -1

            if diff == 0:
                max_length = idx+1
                continue

            if diff in hash_map:
                max_length = max(max_length, idx - hash_map[diff])
            else:
                hash_map[diff] = idx
        
        return max_length