# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], level = 0) -> int:
            if not root:
                return level
            
            left = dfs(root.left, level = level + 1)
            right = dfs(root.right, level = level + 1)

            return max(left, right)
        
        return dfs(root, level = 0)