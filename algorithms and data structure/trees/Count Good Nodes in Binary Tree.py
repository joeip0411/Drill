# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, cur_max):
            nonlocal res

            if not root:
                return
            
            if root.val >= cur_max:
                res += 1
            
            new_max = max(cur_max, root.val)
            
            dfs(root.left, new_max)
            dfs(root.right, new_max)
        
        dfs(root, -float('inf'))

        return res


        