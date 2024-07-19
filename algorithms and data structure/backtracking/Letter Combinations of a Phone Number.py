# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

# in each level of the recursion tree, one subproblem will generate 3-4 subproblems
# height of the decision tree is n
# and we also have to copy the array into the output array which is O(n)
# The overall time complexity is O(n 4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []
        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i >= len(digits):
                if cur:
                    res.append("".join(cur.copy()))
                return

            for letter in hash_map[digits[i]]:
                cur.append(letter)
                backtrack(i+1)
                cur.pop()

        backtrack(0)

        return res