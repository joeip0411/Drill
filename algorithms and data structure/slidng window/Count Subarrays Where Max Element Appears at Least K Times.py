from typing import List


class Solution:
    # find number of subarray where max appears >= k times is equivalent to 
    # finding total number of subarrays - number of subarray where max_item < k times
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_item = max(nums)
        max_count = 0
        res = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == max_item:
                max_count += 1
            
            while max_count >= k and left <= right:
                if nums[left] == max_item:
                    max_count -= 1
                left += 1
            
            res += right - left + 1

        total_count = len(nums) * (len(nums) + 1) // 2

        return total_count - res