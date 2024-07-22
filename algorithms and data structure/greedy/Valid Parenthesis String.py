# https://leetcode.com/problems/valid-parenthesis-string/

# When encountering a close parenthesis, always use an open parenthesis first
# For remaining open parenthesis, check if there is a star with index greater its index
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_paren = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                open_paren.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if open_paren:
                    open_paren.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        for i in range(len(open_paren)-1, -1, -1):
            if star:
                if star[-1] > open_paren[i]:
                    star.pop()
                else:
                    return False
            else:
                return False
        
        return True
    
# Time complexity: O(n)
# Space complexity: O(1)
# keep track of possible ranges of open parenthesis
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min, open_max = 0, 0

        for char in s:
            if char == '(':
                open_min += 1
                open_max += 1
            elif char == ')':
                open_min -= 1
                open_max -= 1
            else:
                open_min -= 1
                open_max += 1

            if open_max < 0:
                return False
            if open_min < 0:
                open_min = 0
    
        valid = open_min <= 0 <= open_max

        return valid