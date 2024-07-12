# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(S T) because we check every node in the main tree against the whole target subtree
# Using BFS
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # do a compare tree for every single node in the main tree

        def compare_tree(root, subroot):
            # both are None
            if not root and not subroot:
                return True
            # one is None
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            
            # the values are equal
            left = compare_tree(root.left, subroot.left)
            right = compare_tree(root.right, subroot.right)

            return left and right
        
        q = deque()

        if root:
            q.append(root)
        
        while q:
            node = q.popleft()
            result = compare_tree(node, subRoot)

            if result is True:
                return result
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
    
# Using DFS
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # do a compare tree for every single node in the main tree

        def compare_tree(root, subroot):
            # both are None
            if not root and not subroot:
                return True
            # one is None
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            
            left = compare_tree(root.left, subroot.left)
            right = compare_tree(root.right, subroot.right)

            return left and right

        if not subRoot:
            return True
        if not root:
            return False

        if compare_tree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right