# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    # store the position of valid paren in set
    # stack to determine whether a paren is valid
    # when interate the string again, if paren, check if the pos is in valid pos, if yes, add to output

    # Time complexity = O(n)
    # Space complexity = O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        
        valid_pos = set()
        stack = []
        res = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    open_paren_pos = stack.pop()
                    valid_pos.add(open_paren_pos)
                    valid_pos.add(i)
        
        for i in range(len(s)):
            if s[i] not in ['(', ')']:
                res.append(s[i])
            else:
                if i in valid_pos:
                    res.append(s[i])
        
        return ''.join(res)