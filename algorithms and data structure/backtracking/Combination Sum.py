# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, cur_sum=0):

            if i >= len(candidates) or cur_sum > target:
                return
            
            if cur_sum == target:
                res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            dfs(i = i, cur_sum = cur_sum + candidates[i])

            cur.pop()
            dfs(i = i + 1, cur_sum = cur_sum)

        dfs(i = 0, cur_sum = 0)
    
        return res