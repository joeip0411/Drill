# https://leetcode.com/problems/subsets-ii/
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    cur = {}

    def dfs(nums, i):
        if i >= len(nums):
            res.append(cur)
 
        cur[nums[i]] = cur.get(nums[i], 0) + 1

        dfs(nums, i+1)

        cur[nums[i]] -= 1

        dfs(nums, i+1)

    dfs(nums, 0)
    res = [list(i) for i in set(res)]
    return res
    
subsetsWithDup([1,2,2])

list((1,2,2))

output = [[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[4,4,4,1,4],[4,1],[4,4,4,1]]
expected = [[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

output.sorted()
expected.sorted()