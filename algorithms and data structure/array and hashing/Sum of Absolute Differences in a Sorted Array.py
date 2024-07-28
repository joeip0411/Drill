# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/

from typing import List


# Everything to the left -> item - left_item
# Everything to the right -> right item - item
# Precompute prefix sum and postfix sum
def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    prefix_sum = [0]
    postfix_sum = [0]

    for i in range(0,len(nums)-1):
        cur = prefix_sum[-1] + nums[i]
        prefix_sum.append(cur)

    for j in range(len(nums)-1, 0, -1):
        cur = postfix_sum[-1] + nums[j]
        postfix_sum.append(cur)
    
    postfix_sum = postfix_sum[::-1]

    res = []

    for i in range(len(nums)):
        left = i * nums[i] - prefix_sum[i]
        right = postfix_sum[i] - (len(nums) - 1 - i) * nums[i]
        temp =  left + right
        res.append(temp)
    
    return res

# Cleaner solution
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        res = []

        for i, num in enumerate(nums):
            right_sum = total - left_sum - num

            left = i * num - left_sum
            right = right_sum - (len(nums) - i - 1) * num
            res.append(left + right)

            left_sum += num
        
        return res