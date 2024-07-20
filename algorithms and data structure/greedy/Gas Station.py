# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    # if sum < 0, return False
    # There is a unique soluion. We just need to calculate the cumulative sum from a position
    # If cumulative sum ever reaches negative, that means all the stations between the starting position and the current position cannot be the valid starting point
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1

        cur_sum = 0
        start_idx = 0
        for i in range(0,len(diff)):
            cur_sum += diff[i]
            if cur_sum < 0:
                cur_sum = 0
                start_idx = i + 1
        
        return start_idx