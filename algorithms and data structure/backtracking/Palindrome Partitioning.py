# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


def partition(s: str) -> List[List[str]]:
    res = []
    cur = []

    def backtrack(start_idx, end_idx):
        print(start_idx, end_idx)
        if start_idx == len(s)-1:
            res.append(cur.copy())
            return
        
        left_substring = s[start_idx:end_idx] 
        print('cur', cur)
        print('left substring', left_substring)
        if left_substring != left_substring[::-1]:
            return
        
        cur.append(left_substring)
        print(cur)

        for i in range(end_idx, len(s)-end_idx+1):
            print(end_idx, end_idx + i)
            print('------------')
            backtrack(end_idx, end_idx + i)
            cur.pop()

    for i in range(1, len(s)+1):
        backtrack(0, i)
    
    return res

partition('aab')