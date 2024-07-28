# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from typing import List


# floor division by 3, if there is remainder add 1.
# Time complexity: O(n)
# Space compelxity: O(n)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        res = 0

        for freq in counter.values():

            if freq == 1:
                return -1

            round_up = 1 if freq % 3 > 0 else 0
            quotient = freq // 3
            count = quotient + round_up
            res += count
        
        return res