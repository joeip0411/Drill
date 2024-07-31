# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
from typing import List


class Solution:
    # find consecutive colors
    # calculate total time and max time for the consecutive colors, add total time - max time to res
    # Time complexity = O(n)
    # Space complexity = O(1)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        left = 0
        right = left + 1

        while right < len(colors):

            total_time = max_time = neededTime[left]

            while right < len(colors) and colors[right] == colors[right - 1]:
                this_time = neededTime[right]
                
                total_time += this_time
                max_time = max(max_time, this_time)

                right += 1
            
            if total_time > max_time:
                res += total_time - max_time
            
            left = right
            right = left + 1
        
        return res