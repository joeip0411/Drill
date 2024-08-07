# https://leetcode.com/problems/validate-stack-sequences/description/

from typing import List


# keep pushing items to stack until there is a match with pop, keep popping until there is no match
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []

        for i in range(len(pushed)):
            stack.append(pushed[i])

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return len(stack) == 0