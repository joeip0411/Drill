# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        cur_sum = 0
        res = 0

        for R in range(len(arr)):
            if R - L + 1 > k:
                cur_sum -= arr[L]
                L += 1

            cur_sum += arr[R]

            if R - L + 1 == k:
                if cur_sum / k >= threshold:
                    res += 1
        
        return res