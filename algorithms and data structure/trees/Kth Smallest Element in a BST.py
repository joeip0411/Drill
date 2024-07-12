# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def in_order(root: Optional[TreeNode]) -> List[int]:

            if not root:
                return []
            
            left = in_order(root.left)
            mid = [root.val]
            right = in_order(root.right)

            return left + mid + right
        
        in_order_list = in_order(root)
        res = in_order_list[k-1]

        return res