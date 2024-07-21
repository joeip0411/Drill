from typing import List

# store first and last occurence of a character
# sort the interval
# merge intervals
# Time complexity = O(n)

def partitionLabels(s: str) -> List[int]:
    hash_map = {}

    # O(n)
    for i in range(len(s)):
        if s[i] not in hash_map:
            hash_map[s[i]] = [i, i]
        else:
            hash_map[s[i]][1] = i
    
    # O(26)
    intervals = sorted([i for i in hash_map.values()])

    merged_intervals = []

    prev = intervals[0]

    # O(26)
    for i in range(1, len(intervals)):
        cur = intervals[i]

        if prev[1] > cur[0]:
            prev = [min(prev[0], cur[0]), max(prev[1], cur[1])]
        else:
            merged_intervals.append(prev)
            prev = cur
    
    merged_intervals.append(prev)

    # O(26)
    res = [i[1] - i[0] + 1 for i in merged_intervals]

    return res

# keeping track and dynamically update end
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        res = []

        for i in range(len(s)):
            hash_map[s[i]] = i
        
        size = 0
        end = -float('inf')

        for i in range(len(s)):
            size += 1
            end = max(end, hash_map[s[i]])

            if end == i:
                res.append(size)
                size = 0
        
        return res