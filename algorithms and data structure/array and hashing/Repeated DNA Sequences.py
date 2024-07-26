# https://leetcode.com/problems/repeated-dna-sequences/description/

from typing import List

# Time complexity = O(n)
# Space complexity = O(n)

# Simply brute force and find all the subtring and add to hash set to find duplicates
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        hash_set = set()

        for i in range(len(s) - 10 + 1):
            substring = s[i: i + 10]
            
            if substring in hash_set:
                res.add(substring)
            else:
                hash_set.add(substring)
        
        return list(res)

