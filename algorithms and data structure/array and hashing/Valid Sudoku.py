# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i:set() for i in range(len(board))}
        col_map = {i:set() for i in range(len(board))}
        grid_map = {(i,j):set() for j in range(len(board)//3) for i in range(len(board)//3 )}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                if board[i][j] not in row_map[i]:
                    row_map[i].add(board[i][j])
                else:
                    return False

                if board[i][j] not in col_map[j]:
                    col_map[j].add(board[i][j])
                else:
                    return False

                if board[i][j] not in grid_map[(i//3,j//3)]:
                    grid_map[(i//3,j//3)].add(board[i][j])
                else:
                    return False
        
        return True

        