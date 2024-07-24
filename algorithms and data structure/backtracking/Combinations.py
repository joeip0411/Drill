# https://leetcode.com/problems/combinations/description/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(num):
            
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            if num > n:
                return
            
            cur.append(num)
            backtrack(num+1)

            cur.pop()
            backtrack(num+1)
        
        backtrack(1)

        return res