# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '':
            return False
        
        s_idx = 0
        t_idx = 0

        while t_idx < len(t) and s_idx < len(s):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1
        
        return s_idx == len(s)