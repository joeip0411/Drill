# https://leetcode.com/problems/find-k-closest-elements/
from typing import List


# Time complexity = O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = left + k - 1

        res_left = left
        res_right = right

        while right + 1 < len(arr):
            if abs(arr[right + 1] - x) < abs(arr[left] - x):
                res_left = left + 1
                res_right = right + 1
            left += 1
            right += 1
        
        return arr[res_left:res_right+1]