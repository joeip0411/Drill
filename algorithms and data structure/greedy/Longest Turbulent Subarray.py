# https://leetcode.com/problems/longest-turbulent-subarray/
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_count = 1
        cur_count = 1

        # less than first
        for i in range(1, len(arr)):
            if (arr[i-1] < arr[i] and i%2 == 1) or (arr[i-1] > arr[i] and i%2 == 0):
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 1

        # greater than first
        cur_count = 1

        for i in range(1, len(arr)):
            if (arr[i-1] < arr[i] and i%2 == 0) or (arr[i-1] > arr[i] and i%2 == 1):
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 1
        
        return max_count
        