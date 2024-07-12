# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def search(board, word, i, j, k):
            if k >= len(word):
                return True
            
            if min(i,j) < 0 \
                or i >= len(board) \
                or j >= len(board[0]) \
                or board[i][j] != word[k] \
                or (i,j) in visited:
                return False
            
            visited.add((i,j))

            up = search(board, word, i-1, j, k+1)
            down = search(board, word, i+1, j, k+1)
            left = search(board, word, i, j-1, k+1)
            right = search(board, word, i, j+1, k+1)
            
            visited.remove((i,j))
        
            return up or down or left or right
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = search(board, word, i, j, 0)
                if res:
                    return True
        
        return False
    

    list((1,2))
