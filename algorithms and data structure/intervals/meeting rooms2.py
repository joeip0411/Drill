"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
            
        hash_map = {}

        for interval in intervals:
            for i in range(interval.start, interval.end):
                hash_map[i] = hash_map.get(i, 0) + 1
        
        return max(hash_map.values())

# sort start and end time respectively
# maintain two pointers, move the pointer when its item is smaller, increment/decrement count accordingly
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start_time = sorted([i.start for i in intervals])
        end_time = sorted([i.end for i in intervals])

        i = 0
        j = 0
        count = 0
        res = 0

        while i < len(start_time):
            if start_time[i] < end_time[j]:
                count += 1
                i += 1
            elif end_time[j] < start_time[i]:
                count -= 1
                j += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        
        return res