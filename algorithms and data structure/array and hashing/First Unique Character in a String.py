# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for idx, val in enumerate(s):
            if val not in hash_map:
                hash_map[val] = idx
            else:
                hash_map[val] = float('inf')
        
        res = float('inf')
        for v in hash_map.values():
            res = min(res, v)
        
        return -1 if res == float('inf') else res