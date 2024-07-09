# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    # most likely a hashing problem
    # find a way to hash the string into the same key if they consist of the same characters

    # total complexity is O(NK) where N is the average length of word, and K is the number of word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hash_func(text) -> str:
            arr = [0] * 26 # O(1)

            for char in text: # O(n)
                arr[ord(char) - ord('a')] += 1
            
            return '|'.join([str(i) for i in arr]) # O(1)

        hash_map = {}

        for word in strs:
            key = hash_func(word) # O(n)
            if key not in hash_map:
                hash_map[key] = [word]
            else:
                hash_map[key].append(word)
        
        return hash_map.values()
