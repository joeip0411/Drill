# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        q = deque()

        if root:
            q.append(root)
        
        while q:
            this = []
            for i in range(len(q)):
                node = q.popleft()
                this.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(this)
        
        return res