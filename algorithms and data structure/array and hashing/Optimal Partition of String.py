# https://leetcode.com/problems/optimal-partition-of-string/

# Just hash set to keep track of character seen

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 1
        
        for char in s:
            if char in seen:
                res += 1
                seen = set()

            seen.add(char)
        
        return res

