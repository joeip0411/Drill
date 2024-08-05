# https://leetcode.com/problems/find-k-closest-elements/
from typing import List


# See whether the right element to the window is closer to the start element
# Update result window if yes
# Time complexity = O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = left + k - 1

        res_left = left
        res_right = right

        while right + 1 < len(arr):
            if abs(arr[right + 1] - x) < abs(x - arr[left]):
                res_right = right + 1
                res_left = left + 1
            right += 1
            left += 1

            if arr[left] > x:
                return arr[res_left: res_right + 1]
        
        return arr[res_left: res_right + 1]
    
# Using binary search
# Time complexity = O(log n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (right + left) // 2

            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        
        return arr[left: left + k]
