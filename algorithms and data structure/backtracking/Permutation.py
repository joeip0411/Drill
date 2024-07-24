# https://leetcode.com/problems/permutations/
from typing import List

# at each level, each subproblem will have to do 1,2,3...n comparison,
# so the overall time complexity is O(n! x n^2)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        hash_set = set()

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i not in hash_set:
                    cur.append(nums[i])
                    hash_set.add(i)

                    backtrack()
                    cur.pop()
                    hash_set.remove(i)
            
        backtrack()
        return res