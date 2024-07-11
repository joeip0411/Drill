from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast slow algorithm to find mid point
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # beginning if second half
        mid = slow.next
        # set next pointer of the last node in the new list to None
        slow.next = None
        
        # reversing the second half
        prev = None
        cur = mid

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # merge the two list
        this = head
        other = prev
        
        while this and other:
            nxt = this.next
            this.next = other
            this = nxt
            this, other = other, this
            
        return head