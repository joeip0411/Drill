from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()

        for n in nums: # O(n)
            hash_set.add(n)
        
        longest_sequence = 0

        for n in hash_set: # O(n), each item can be probed 2 times max

            # find start of a seuqnce
            if n - 1 in hash_set:
                continue

            cur_seq_length = 1
            nxt = n + 1

            while nxt in hash_set:
                cur_seq_length += 1
                nxt += 1
            
            if cur_seq_length > longest_sequence:
                longest_sequence = cur_seq_length
        
        return longest_sequence