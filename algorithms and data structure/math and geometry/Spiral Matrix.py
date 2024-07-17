# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        cur_row = 0
        cur_col = 0
        up = left = 0
        down = len(matrix)-1
        right = len(matrix[0]) - 1
        size = len(matrix) * len(matrix[0])
        res = []

        while count < size:
            # right
            while cur_col <= right and count < size:
                res.append(matrix[cur_row][cur_col])
                count += 1
                cur_col += 1

            cur_col -= 1
            cur_row += 1

            # down
            while cur_row <= down and count < size:
                res.append(matrix[cur_row][cur_col])
                count += 1
                cur_row += 1

            cur_row -= 1
            cur_col -= 1

            # left
            while cur_col >= left and count < size:
                res.append(matrix[cur_row][cur_col])
                count += 1
                cur_col -= 1
            
            cur_col += 1
            cur_row -= 1

            up += 1

            # up
            while cur_row >= up and count < size:
                res.append(matrix[cur_row][cur_col])
                count += 1
                cur_row -= 1 
            
            cur_row += 1
            cur_col += 1

            left += 1
            right -= 1
            down -= 1
        
        return res