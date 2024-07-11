# https://leetcode.com/problems/longest-repeating-character-replacement/

# the main for a window to be valid is to maintain
# window size - most frequent item count <= k, i.e. we don't want to replace the most frequent item

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 0
        hash_map = {}
        max_length = 0

        while right < len(s):
            hash_map[s[right]] = 1 + hash_map.get(s[right], 0)
            
            while (right - left + 1) - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length