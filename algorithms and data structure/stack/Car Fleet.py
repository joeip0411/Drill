# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
from typing import List


# sort car by position
# if time required to reach target of current car is less than next car, that means it must be blocked by the next car
# in this case, whether the current car is present does not matter
# if the current car is not block by the next car, than it becomes the item to compare.
# Time complexity = O(n log n)
# Space complexity = O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = sorted([(position[i], speed[i]) for i in range(len(speed))], reverse = True)

        stack = []

        for c in combine:
            stack.append(c)

            if len(stack) >= 2:
                # time = distance / speed
                this_time = (target - stack[-1][0]) / stack[-1][1]
                prev_time = (target - stack[-2][0]) / stack[-2][1]

                if this_time <= prev_time:
                    stack.pop()
        
        return len(stack)