# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


# split a string into left and right substring. If left substring is a palindrome,
# recursively check if the right substring is also a palindrome
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def backtrack(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            
            # generate left substring of different length
            for j in range(i+1, len(s)+1):
                # if left substring is a palindrome
                if s[i:j] == s[i:j][::-1]:
                    cur.append(s[i:j])
                    # recursively check if the right substring is also a palindrome
                    backtrack(j)
                    cur.pop()
            
        backtrack(0)
        return res
            