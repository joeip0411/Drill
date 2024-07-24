# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


# If there is a duplciate, that means a node must be pointed by at least 2 nodes. This is afind the start of linked list cycle problem.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                new_head = nums[0]

                while slow != new_head:
                    slow = nums[slow]
                    new_head = nums[new_head]
                
                return slow