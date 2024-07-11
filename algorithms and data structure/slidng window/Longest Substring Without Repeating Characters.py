# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# The idea is to move the start pointer to the next item of the duplicate
# reduce the current sequence count by the number of unit shifted
# we can use a dictionary to keep track whether a duplicate item is found and its corresponding position
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, i = 0, 0
        max_length, cur_length = 0, 0
        hash_map = {}

        while i < len(s):
            # char not in current seq
            if hash_map.get(s[i], -1) < start:
                cur_length += 1
            else:
                # reduce cur_length by the number of units shifted
                cur_length = cur_length - (hash_map.get(s[i]) - start)
                # exclude the duplicate and all items before it
                start = hash_map.get(s[i]) + 1
                
            hash_map[s[i]] = i
            max_length = max(max_length, cur_length)
            i += 1
        
        return max_length