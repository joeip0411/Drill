# https://leetcode.com/problems/fruit-into-baskets/description/

from collections import defaultdict
from typing import List


# Remove existing item from basket before adding if both baskets are non empty
# Time complexity = O(n)
# Space complexity = O(1)
def totalFruit(fruits: List[int]) -> int:
    left = right = 0
    hash_map = defaultdict(int)
    res = 0

    while right < len(fruits):
        # remove item from basket if not enough space
        while len(hash_map) == 2 and fruits[right] not in hash_map:
            remove_fruit = fruits[left]

            hash_map[remove_fruit] -= 1
            if hash_map[remove_fruit] == 0:
                del hash_map[remove_fruit]
            left += 1

        add_fruit = fruits[right]
        hash_map[add_fruit] += 1
        res = max(res, right - left + 1)
        right += 1

    return res