# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Find mid point, reverse second half, calculate twin sum
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_head = slow.next
        slow.next = None

        prev = None
        cur = new_head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        new_head = prev

        max_twin_sum = -float('inf')
        while head:
            max_twin_sum = max(max_twin_sum, head.val + new_head.val)
            head = head.next
            new_head = new_head.next
        
        return max_twin_sum