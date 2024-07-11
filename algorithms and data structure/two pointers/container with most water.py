from typing import List

# moving the higher pointer can only decrease the area
# therefore, to find the max area, we can only move the smaller pointer

class Solution:

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area