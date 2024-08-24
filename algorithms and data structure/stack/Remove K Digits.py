# https://leetcode.com/problems/remove-k-digits/

# if current item less than top of stack, pop stack

# pop from stack if k > 0 after appending item to stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            
            if not stack and n == '0':
                continue
            
            stack.append(n)

        while stack and k > 0:
            stack.pop()
            k -= 1

        res = ''.join(stack) if stack else '0'

        return res