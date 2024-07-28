# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from typing import List


# counter all item
# start from highest frequency, append to res
# carry previous result to current result
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        reverse_counter = {}

        for k,v in counter.items():
            if v not in reverse_counter:
                reverse_counter[v] = [k]
            else:
                reverse_counter[v].append(k)
        
        res = []

        for i in range(len(nums), 0, -1):
            prev = res[-1] if len(res) > 0 else []
            cur = prev + reverse_counter.get(i, [])
            
            if cur:
                res.append(cur)

        return res
    
# count frequency of items, populate res on the fly
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        res = []

        for n in nums:
            if n not in counter:
                counter[n] = 0

            row = counter[n]

            if row == len(res):
                res.append([])
            
            res[row].append(n)
            counter[n] += 1
        
        return res