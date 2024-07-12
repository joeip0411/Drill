# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) <= 0:
            return
        
        node = TreeNode(val = preorder[0])

        split_index = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:split_index+1], inorder[:split_index])
        node.right = self.buildTree(preorder[split_index+1:], inorder[split_index+1:])

        return node