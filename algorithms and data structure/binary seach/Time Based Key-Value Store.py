# https://leetcode.com/problems/time-based-key-value-store/

# This question is a good example of doing range search using binary search
# We continue doing binary search even when the condition is satisfy
# This is to look for a larger / smaller value that satisfy the criteria

class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        item = ""
        if key not in self.hash_map:
            return item
        
        left = 0
        right = len(self.hash_map[key]) - 1
        self.hash_map[key].append((float('inf'), ''))

        while left <= right:
            mid = (left + right) // 2
            if self.hash_map[key][mid][0] <= timestamp and self.hash_map[key][mid+1][0] > timestamp:
                self.hash_map[key].pop()
                return self.hash_map[key][mid][1]
            elif self.hash_map[key][mid][0] < timestamp and self.hash_map[key][mid+1][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        self.hash_map[key].pop()
        return item
    
class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key] = self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        item = ""
        if key not in self.hash_map:
            return item
        
        values = self.hash_map[key]

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            # continue to see if there are any greater items
            if values[mid][0] <= timestamp:
                # store valid result seen so far
                item = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return item