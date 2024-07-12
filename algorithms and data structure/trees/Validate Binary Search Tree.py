# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid_BST_with_bounds(root, lowerbound, upperbound) -> bool:
            if not root:
                return True
            
            if root.left and not lowerbound < root.left.val < root.val:
                return False
            
            if root.right and not root.val < root.right.val < upperbound:
                return False

            left = is_valid_BST_with_bounds(root.left, lowerbound, root.val)
            right = is_valid_BST_with_bounds(root.right, root.val, upperbound)

            return left and right
        
        return is_valid_BST_with_bounds(root, -float('inf'), float('inf'))