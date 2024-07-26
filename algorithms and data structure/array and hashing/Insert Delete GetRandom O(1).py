# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            idx = len(self.array)
            self.hash_map[val] = idx
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        else:
            # replace item to be removed with last item
            # update index of last item
            idx = self.hash_map[val]
            last_item = self.array[len(self.array)-1]
            self.array[idx] = last_item
            self.hash_map[last_item] = idx
            
            self.array.pop()
            del self.hash_map[val]

            return True
            
    def getRandom(self) -> int:
        idx = random.randint(0, len(self.array)-1)
        res = self.array[idx]
        return res
