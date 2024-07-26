# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
from typing import List


class Solution:
    # Brute force will be O(n^2) where we compare every possible pair of i and j
    # Use a hash map to count the frequency of each ratio
    # e.g. if frequency is 4, that means there will be 3+2+1 matches

    # Time complexity = O(n)
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        hash_map = {}
        res = 0

        for r in rectangles:
            ratio = r[0]/r[1]
            hash_map[ratio] = hash_map.get(ratio, 0) + 1
        
        for v in hash_map.values():
            matches = v * (v-1) // 2
            res += matches
        
        return res


        