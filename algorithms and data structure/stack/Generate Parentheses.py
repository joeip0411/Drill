# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


# we can add an open paranthesis at anytime
# can only add a close parenthsis if the count of open paren  > count of close paren
# Time complexity is O(2^n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate_paren_recur(open_left, close_left, cur):
            if open_left == 0 and close_left == 0:
                res.append(cur)
                return
            
            if open_left > 0:
                generate_paren_recur(open_left -1, close_left, cur + '(')
            if close_left > 0 and open_left < close_left:
                generate_paren_recur(open_left, close_left-1, cur + ')')
        
        generate_paren_recur(n,n,'')
        return res