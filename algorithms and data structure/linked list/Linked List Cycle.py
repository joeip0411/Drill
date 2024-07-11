# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(n), Space complexity: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()

        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next

        return False
    
    # Fast & Slow pointer: Time complexity: O(n), Space complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False