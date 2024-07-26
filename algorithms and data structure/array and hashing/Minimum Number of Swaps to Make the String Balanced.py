# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

# count number of out of order brackets
# each swap can fix 1-2 out of order brackets
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        open_paren = 0
        out_order = 0

        for char in s:
            if char == '[':
                open_paren += 1
            else:
                if open_paren <= 0:
                    out_order += 1
                else:
                    open_paren -= 1
        
        res = out_order % 2 + out_order // 2

        return res