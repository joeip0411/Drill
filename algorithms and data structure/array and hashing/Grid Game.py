# https://leetcode.com/problems/grid-game/
from typing import List


# Blue will get the higher of the postifx of row 1 or prefix of row 2
# Red will try to minimise blue's point, so this is a prefix sum problem with the minimax concept
# Time complexity = O(n)
# Space complexity = O(n)
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        prefix = grid[1].copy()
        postfix = grid[0].copy()

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        for i in range(len(postfix)-2, -1, -1):
            postfix[i] += postfix[i+1]

        min_max_point = float('inf')

        for i in range(len(grid[0])):
            up_point = postfix[i+1] if i+1 < len(grid[0]) else 0
            down_point = prefix[i-1] if i-1 >= 0 else 0
            blue_point = max(up_point, down_point)
            min_max_point = min(min_max_point, blue_point)
        
        return min_max_point