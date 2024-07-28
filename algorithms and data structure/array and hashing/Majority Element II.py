import math
from typing import List


# count freq of the 2 most frequent item, if current item not in counter, all item in counter -= 1
# if count == 0, remove item from counter
# The idea of the algo is, if we encounter 1:1,2:1 and now 3:1, we don't care about all the item that is <= 1/3, 
# so we evict all the item, i.e. decrement the count by 1, if count == 0, remove item. Same as majority item case.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}

        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                if len(counter) < 2:
                    counter[n] = 1
                else:
                    remove = set()

                    for k in counter:
                        counter[k] -= 1
                        
                        if counter[k] == 0:
                            remove.add(k)
                    
                    for k in remove:
                        del counter[k]
        
        res_count = {}
        res = set()
        
        for n in nums:
            if n in counter:
                res_count[n] = res_count.get(n, 0) + 1
                if res_count[n] > math.floor(len(nums) / 3):
                    res.add(n)
        
        return list(res)

# A clenar solution, create new dict with decremented frequency instead of removing from existing dict.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1

            if len(counter) > 2:
                new_counter = {}

                for k, v in counter.items():
                    if v > 1:
                        new_counter[k] = v - 1
                        
                counter = new_counter

        res_count = {}
        res = set()
        
        for n in nums:
            if n in counter:
                res_count[n] = res_count.get(n, 0) + 1
                if res_count[n] > math.floor(len(nums) / 3):
                    res.add(n)
        
        return list(res)