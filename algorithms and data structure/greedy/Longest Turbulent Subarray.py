# https://leetcode.com/problems/longest-turbulent-subarray/
from typing import List


# Time complexity = O(n)
# Space complexity = O(1)
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
    
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        max_size = 1
        prev = ''

        while r < len(arr):
            if arr[r] < arr[r-1] and prev != '<':
                max_size = max(max_size, r - l + 1)
                r += 1
                prev = '<'
            elif arr[r] > arr[r-1] and prev != '>':
                max_size = max(max_size, r - l + 1)
                r += 1
                prev = '>'
            else:
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r - 1
                prev = ''
        
        return max_size
                