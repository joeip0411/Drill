# https://leetcode.com/problems/permutations/
from typing import List

# at each level, each subproblem will have to do 1,2,3...n comparison,
# so the overall time complexity is O(n! x n^2)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                backtrack()
                cur.pop()
        
        backtrack()
        return res