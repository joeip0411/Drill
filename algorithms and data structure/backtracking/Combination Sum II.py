# https://leetcode.com/problems/combination-sum-ii/

from typing import List


# filter out candidates that are greater than target at the beginning
# terminate early if sum is already greater than target
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted([i for i in candidates if i <= target])
        res = []
        cur = []
        cur_sum = [0]

        def dfs(i):
            if cur_sum[0] > target:
                return
                
            if i >= len(candidates):
                if cur_sum[0] == target:
                    res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            cur_sum[0] += candidates[i]

            dfs(i+1)

            cur.pop()
            cur_sum[0] -= candidates[i]

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1)
        
        dfs(0)
        return res