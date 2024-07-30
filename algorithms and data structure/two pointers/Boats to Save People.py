# https://leetcode.com/problems/boats-to-save-people/

from typing import List


# Max 2 people per boat.
# Always pick the heaviest person, if there is room for lightest people, then also add.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        res = 0

        while left <= right:
            temp_limit = limit
            temp_limit -= people[right]
            right -= 1

            if left <= right and temp_limit >= people[left]:
                left += 1
            
            res += 1
        
        return res
            