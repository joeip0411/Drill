from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# maintain mapping of old and new nodes
# Traverse the link list to make a copy
# Traverse another time to set the random pointer

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        prev = dummy

        cur = head
        hash_map = {}
        
        while cur:
            val = cur.val
            new_node = Node(val)
            prev.next = new_node
            prev = new_node

            hash_map[cur] = new_node
            
            cur = cur.next
        
        cur = head
        new_cur = dummy.next

        while cur:
            random = cur.random
            new_random = hash_map.get(random, None)
            new_cur.random = new_random

            cur = cur.next
            new_cur = new_cur.next
        
        return dummy.next