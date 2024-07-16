from typing import List

# Brute Froce approach is O(n^2)

# Time Complexity: O(n)
# Space Complexity: O(1)

# As long as the carrying value is positive, it is worthwhile to carry over, otherwise reset carrying value to current item

def maxSubArray(self, nums: List[int]) -> int:
    res = -float('inf')
    prev_sum = -float('inf')

    for num in nums:
        prev_sum = max(num, num + prev_sum)
        res = max(res, prev_sum)
    
    return res