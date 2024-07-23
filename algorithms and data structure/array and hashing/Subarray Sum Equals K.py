# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List


# Keep track of count of all prefix sum
# After we calculate a new prefix sum, see if we have any prefix sum such that new prefix sum - existing prefix sum = k
# if so, then there are some subarray that sums to k. We increment results by the count of existing prefix sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        hash_map = {0: 1}

        for n in nums:
            prefix_sum += n
            res += hash_map.get(prefix_sum - k, 0)
            hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
        
        return res