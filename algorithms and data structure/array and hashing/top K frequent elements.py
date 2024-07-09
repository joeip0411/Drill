# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from typing import List


# hash map to keep track of frequency
# max heap to find the top frequent items
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}

        for n in nums: # O(n)
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        
        arr = [[-v,k] for k,v in freq_map.items()] # O(n)

        heapq.heapify(arr) # O(n)

        res = []

        for i in range(k): # O(k)
            res.append(heapq.heappop(arr)[1])
        
        return res
    

# Using count sort
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}

        for n in nums: # O(n)
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        
        counter = [[] for i in range(len(nums)+1)] # O(n)

        for key,val  in freq_map.items(): # O(n)
            counter[val].append(key)
        
        res = []

        for i in range(len(counter)-1, -1, -1): # O(n)
            if k <= 0:
                break
            
            if len(counter[i]) >= 1:
                res = res + counter[i]
                k -= len(counter[i])
        
        return res
        