# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List



class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -float('inf')
        res = [0] * len(arr)
        res[-1] = -1

        for i in range(len(arr)-1, 0, -1):
            max_num = max(max_num, arr[i])
            res[i-1] = max_num

        return res