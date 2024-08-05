# https://leetcode.com/problems/get-equal-substrings-within-budget/

# extend right pointer to include an extra character
# if cost exceeds maxCost, move left pointer to the right and reduce current cost
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = 0
        cur = 0
        res = 0

        for right in range(len(s)):
            cur += abs(ord(s[right]) - ord(t[right])) 
            
            while cur > maxCost and left <= right:
                cur -= abs(ord(s[left]) - ord(t[left])) 
                left += 1

            res = max(res, right - left + 1)
            
        return res