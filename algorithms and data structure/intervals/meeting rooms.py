# https://neetcode.io/problems/meeting-schedule

from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Using hashset
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        hash_set = set()

        for intvl in intervals:
            for i in range(intvl.start, intvl.end):
                if i not in hash_set:
                    hash_set.add(i)
                else:
                    return False
        
        return True

# Using sorting
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)

        for i in range(len(intervals) - 1):
            if intervals[i+1].start < intervals[i].end:
                return False
        
        return True
    


l = []

if l:
    print('true')