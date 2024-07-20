# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        res = ListNode()
        cur = res

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            two_sum = val1 + val2 + carry
            
            if two_sum >= 10:
                carry = 1
                two_sum -= 10
            else:
                carry = 0
            
            cur.next = ListNode(two_sum)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            cur.next = ListNode(1)
            cur = cur.next
        
        return res.next
            