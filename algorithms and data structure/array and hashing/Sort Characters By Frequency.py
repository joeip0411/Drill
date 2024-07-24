# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map  = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        
        sorted_char = sorted([[freq, key] for key, freq in hash_map.items()], reverse = True)

        res = []
        for freq, key in sorted_char:
            res.append(key * freq) 
        
        return ''.join(res)

# reversing the frequency and char in hash map to build final result
class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map  = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        
        freq_map = {}

        for key, freq in hash_map.items():
            if freq not in freq_map:
                freq_map[freq] = []
            freq_map[freq].append(key)
        
        res = []

        for i in range(len(s), 0, -1):
            if i in freq_map:
                for char in freq_map[i]:
                    res.append(i * char)
        
        return ''.join(res)
    
    hash('123')