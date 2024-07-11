# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2 passes
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        cur = dummy.next

        node_count = 0

        while cur:
            node_count += 1
            cur = cur.next
        
        prev = dummy
        cur = dummy.next

        while node_count - n > 0:
            prev = cur
            cur = cur.next
            node_count -= 1
        
        prev.next = cur.next

        return dummy.next

# 1 pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        left = right = dummy

        while n + 1 > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
