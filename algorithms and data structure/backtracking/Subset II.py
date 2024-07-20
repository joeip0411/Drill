# https://leetcode.com/problems/subsets-ii/
from typing import List


# Using dict to keep track of frequency and set to deduplicate
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    hash_set = set()
    cur = {}

    def dfs(nums, i):
        if i >= len(nums):
            
            values = tuple(sorted(cur.items()))

            if values not in hash_set:
                hash_set.add(values)

            return
        
        cur[nums[i]] = cur.get(nums[i], 0) + 1

        dfs(nums, i + 1)

        cur[nums[i]] -= 1

        dfs(nums, i+ 1)
    
    dfs(nums, 0)

    res = []
    for comb in hash_set:
        temp = []
        for key, freq in comb:
            for _ in range(freq):
                temp.append(key)
        res.append(temp)

    return res

# sort the array
# if we decide the skip the current item, we must also skip all the subsequent item with the same value
# e.g. [1,1,2,3]. In the left path, we have [1,_,2,3]. If we decide to skip the first item, we can have
# [_,1,2,3], which is a duplicate.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(nums, i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])

            dfs(nums, i + 1)

            cur.pop()

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(nums, i+ 1)
        
        dfs(nums, 0)

        return res