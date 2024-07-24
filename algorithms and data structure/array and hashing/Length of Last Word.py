# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        start = len(s)-1

        while s[start] == ' ':
            start -= 1

        for i in range(start, -1, -1):
            if s[i] == ' ':
                break
            res += 1
        
        return res