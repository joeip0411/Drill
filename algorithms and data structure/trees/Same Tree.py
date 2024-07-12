from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using preorder and inorder traversal
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(root) -> List[int]:
            if not root:
                return [None]
            
            mid = [root.val]
            left = preorder(root.left)
            right = preorder(root.right)

            return mid + left + right
        
        def inorder(root) -> List[int]:
            if not root:
                return [None]

            left = preorder(root.left)
            mid = [root.val]
            right = preorder(root.right)

            return left + mid + right
        
        return preorder(p) == preorder(q) and inorder(p) == inorder(q)

# Using BFS
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1 = deque()
        q2 = deque()

        if p:
            q1.append(p)
        if q:
            q2.append(q)
        
        while q1 and q2:
            p_item = q1.popleft()
            q_item = q2.popleft()

            # one is TreeNode, the other is None
            if type(p_item) != type(q_item):
                return False
            # both are TreeNode
            elif p_item:
                # if val is different return False immediately
                if p_item.val != q_item.val:
                    return False

                q1.append(p_item.left)
                q1.append(p_item.right)
                q2.append(q_item.left)
                q2.append(q_item.right)
        
        return len(q1) == len(q2) == 0
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # both are None
        if not p and not q:
            return True
        # one is None
        if not p or not q:
            return False
        # both are Node and value not equal
        if p.val != q.val:
            return False
        
        # if both values are the same, traverse tree recursively
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right