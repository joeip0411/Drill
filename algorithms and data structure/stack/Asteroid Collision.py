from typing import List


class Solution:
    # append positive asteroid to stack
    # keep popping from stack if abs of negative asteroid is greater than positive asteroids on stack
    # append negative asteroid to stack if it has not been destroyed after popping
    # Time complexity = O(n)
    # Space complexity = O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0 or (not stack and a < 0):
                stack.append(a)
            elif a < 0:
                destroyed = False

                while stack and stack[-1] > 0 and not destroyed:
                    last_item = abs(stack[-1])
                    if abs(a) >= last_item:
                        stack.pop()
                    if abs(a) <= last_item:
                        destroyed = True
   
                if not destroyed:
                    stack.append(a)
                    
        return stack