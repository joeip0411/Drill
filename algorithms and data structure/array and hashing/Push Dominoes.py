# https://leetcode.com/problems/push-dominoes/

from collections import deque



# Using queue to simulate domino effect one step at a time
# Dominoes are pushed to queue from left to right
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = deque()

        # add to queue from left to right
        for idx, val in enumerate(dominoes):
            if val != '.':
                q.append((idx,val))
        
        while q:
            idx, val = q.popleft()

            if val == 'L':
                # item to the left is "."
                if idx - 1 >= 0 and dominoes[idx - 1] == '.':
                    dominoes[idx - 1] = 'L'
                    q.append((idx - 1, 'L'))
            elif val == 'R':
                # item to the right is "."
                if idx + 1 < len(dominoes) and dominoes[idx + 1] == '.':
                    if idx + 2 < len(dominoes) and dominoes[idx + 2] == 'L':
                        # if not pop R.L will become RLL
                        q.popleft()
                    else:
                        dominoes[idx + 1] = 'R'
                        q.append((idx + 1, 'R'))
        
        res = ''.join(dominoes)
        return res
