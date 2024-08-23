# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# Time complexity = O(n)
# Space complexity = O(n)
# if char == top item on stack, merge
# pop from stack when freq == k
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ''

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                cur = [char, 1]
                stack.append(cur)
        
        for char, freq in stack:
            res += char * freq
        
        return res