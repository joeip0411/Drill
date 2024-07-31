# https://leetcode.com/problems/k-th-symbol-in-grammar/

# Augmented binary search problem
# The problem can be represented as a tree
# left child is the same as the parent, right child is the reverse of the parent
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left = 1
        right = 2 ** (n - 1)
        cur = 0

        for _ in range(n - 1):
            mid = (right + left) // 2

            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur == 1 else 1
        
        return cur