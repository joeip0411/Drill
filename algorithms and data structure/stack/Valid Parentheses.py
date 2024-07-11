class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for paren in s:
            if paren not in hash_map:
                stack.append(paren)
            else:
                # empty stack or not matching
                if len(stack) <= 0 or hash_map[paren] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0