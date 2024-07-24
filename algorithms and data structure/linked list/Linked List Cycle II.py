# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                another_head = head

                while another_head != slow:
                    slow = slow.next
                    another_head = another_head.next
                
                return slow

        return