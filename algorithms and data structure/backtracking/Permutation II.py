# https://leetcode.com/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        hash_set = set()
        nums.sort()

        def backtrack():
            if len(hash_set) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i not in hash_set:
                    # only select item with same value if the previous ones have been selected
                    if (i == 0) or (i - 1 in hash_set and nums[i] == nums[i-1]) or (nums[i] != nums[i-1]):
                        hash_set.add(i)
                        cur.append(nums[i])

                        backtrack()
                        cur.pop()
                        hash_set.remove(i)
                
        backtrack()
        return res



