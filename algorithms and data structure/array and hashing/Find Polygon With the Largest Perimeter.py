from typing import List


# Prefix sum questions
# Sort array in descending order
# Determine polygon condition for largest side
# Time complexity = O(n log n)
# Space complexity = O(n)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        postfix = nums.copy()

        for i in range(len(postfix)-2, -1, -1):
            postfix[i] += postfix[i+1]
        
        for i in range(len(postfix)-2):
            if nums[i] < postfix[i] - nums[i]:
                return postfix[i]

        return -1

# start from smallest item and determine polygon condition
# Time complexity = O(n log n)
# Space complexity = O(1)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        total = 0
        param = -1

        for i in range(len(nums) - 1):
            total += nums[i]

            # This is not required, because items are sorted, 
            # The last if block will never be true for the first item
            if i < 1:
                continue
            
            if total > nums[i+1]:
                param = total + nums[i+1]
        
        return param
            