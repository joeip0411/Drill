# https://leetcode.com/problems/removing-stars-from-a-string/

# Classic stack problem, nothing special
# Time complexity = O(n)
# Space complexity = O(n)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        return ''.join(stack)