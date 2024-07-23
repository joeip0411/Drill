# https://leetcode.com/problems/contains-duplicate-ii/description/

# Time complexity = O(n)
# Space complexity = O(k)
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                hash_set.remove(nums[L])
                L += 1
            if nums[R] in hash_set:
                return True
            hash_set.add(nums[R])
        
        return False
    
    