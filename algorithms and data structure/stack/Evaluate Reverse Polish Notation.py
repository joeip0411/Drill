# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]

        for i in range(1, len(tokens)):
            if tokens[i] in ('+', '-', '*', '/'):
                item2 = stack.pop()
                item1 = stack.pop()

                if tokens[i] == '+':
                    result = item1+item2
                elif tokens[i] == '-':
                    result = item1 - item2
                elif tokens[i] == '*':
                    result = item1 * item2
                else:
                    if item1 % item2 != 0 and item1 / item2 < 0:
                        result = item1//item2 + 1
                    else:
                        result = item1//item2
                
                stack.append(result)
            else:
                stack.append(int(tokens[i]))


        return stack[0]

