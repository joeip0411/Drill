# https://leetcode.com/problems/invert-binary-tree/description/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        
        if root:
            q.append(root)

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            node.left, node.right = node.right, node.left
        
        return root
    
# dfs with recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is not None:
    
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root