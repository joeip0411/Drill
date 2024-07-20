# https://leetcode.com/problems/task-scheduler/

import heapq
from collections import deque
from typing import List


# sort the task list and determine priority
# if priority <= clock, then pop from heap
# Time complexity  = O(nlogn)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks.sort()

        priority = [1]

        for i in range(1,len(tasks)):
            if tasks[i] == tasks[i-1]:
                p = priority[i-1] + n + 1
            else:
                p = 1
            priority.append(p)
        
        heapq.heapify(priority)

        clock = 1

        while priority:
            if priority[0] <= clock:
                heapq.heappop(priority)
            
            clock += max(1, priority[0] - clock) if priority else 1
        
        return clock - 1

# counter number of each letters
# build max heap for the count, popping the max will yield the lowest processing time
# if val - 1 > 0, means still have pending task, need to add back to the heap
# use a queue to store the pending task, and push back to the heap when the time comes
# continue the algorithm when either the heap or queue still has item.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1
        
        heap = [-i for i in counter.values()]

        heapq.heapify(heap)

        q = deque()

        clock = 1

        while heap or q:
            if heap:
                item = heapq.heappop(heap)
                if item + 1 < 0:
                    q.append((item + 1, clock + n))
                
            while q:
                if q[0][1] == clock:
                    heapq.heappush(heap, q.popleft()[0])
                else:
                    break
            
            clock += 1
        
        return clock - 1
