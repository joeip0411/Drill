# https://leetcode.com/problems/merge-intervals/description/

from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []

    cur_start, cur_end = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i][0] > cur_end:
            res.append([cur_start, cur_end])
            cur_start, cur_end = intervals[i]
        else:
            cur_end = max(cur_end, intervals[i][1])

    res.append([cur_start, cur_end])

    return res

