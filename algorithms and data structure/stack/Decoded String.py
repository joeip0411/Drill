# https://leetcode.com/problems/decode-string/description/

# keep appending to stack if char != ']'
# keep popping to find letters
# pop open parenthesis
# keep popping to find quantifiers
# add back to stack

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        digits = [str(i) for i in range(0,10)]

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                letters = ''
                while stack and stack[-1] != '[':
                    top = stack.pop()
                    letters = top + letters

                # remove open paranthesis
                stack.pop()

                quantifier = ''
                while stack and stack[-1] in digits:
                    top = stack.pop()
                    quantifier = top + quantifier
                quantifier = int(quantifier)

                decoded = quantifier * letters
                stack.append(decoded)


        return ''.join(stack)