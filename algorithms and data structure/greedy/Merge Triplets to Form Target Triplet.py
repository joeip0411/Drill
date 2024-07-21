from typing import List


class Solution:
    # all the triplet that contains an element which is greater than the target will not be considered
    # keep merging and compare to target at the end
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-float('inf'), -float('inf'),-float('inf')]

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                res = [max(res[0], t[0]), max(res[1], t[1]), max(res[2], t[2])]
        
        if res == target:
            return True
        
        return False