import heapq
from typing import List


class Solution:
    # count frequency of each item and put into hash map
    # Use min heap to keep track of the minimum item
    # if frequency of the item becomes 0 and the current item is the min, pop from min heap

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = {}
        for h in hand:
            counter[h]  = counter.get(h,0) + 1

        heap = [k for k in counter.keys()]
        heapq.heapify(heap)

        while heap:
            start = heap[0]
            counter[start] -= 1

            if counter[start] == 0:
                heapq.heappop(heap)
            
            for i in range(1,groupSize):
                if counter.get(start + i, 0) > 0:
                    counter[start + i] -= 1

                    if counter[start + i] == 0 and heap[0] == start + i:
                        heapq.heappop(heap)

                else:
                    return False
        
        return True


