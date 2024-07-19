# https://leetcode.com/problems/partition-equal-subset-sum/description/

from typing import List

# brute force solution
# Calculate total sum, and combination sum, if total sum - combination sum == combination sum, then true
# Time complexity is O(2^n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cur_sum = [0]
        total_sum = sum(nums)
        res = [False]

        def backtrack(i):
            if cur_sum[0] > total_sum - cur_sum[0]:
                return
            if i >= len(nums):
                if cur_sum[0] == total_sum - cur_sum[0]:
                    res[0] = True
                return
            
            cur_sum[0] += nums[i]
            backtrack(i+1)
            cur_sum[0] -= nums[i]
            backtrack(i+1)
        
        backtrack(0)
        return res[0]
    
# Dynamic programming, caching existing combination sum
# for each number, we iterate over the cache, the size of the cache is at most the sum of the whole input array
# Time complexity is O(n sum(num))
# Space complexity is O(sum(num))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        dp  = set()

        for i in range(len(nums)-1, -1,-1):
            if nums[i] == target:
                return True
            new_set = set()

            for combination_sum in dp:
                res = combination_sum + nums[i]
                if res == target:
                    return True
                elif res > target:
                    continue
                new_set.add(res)

            new_set.add(nums[i])
            dp = dp.union(new_set)
        
        return False
