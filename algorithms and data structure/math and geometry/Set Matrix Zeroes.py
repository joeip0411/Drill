# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

# the order of operations matters a lot in this question
# we mark the row header and column header to 0 if the current cell is 0
# allocate an extra variable to indicate whether the first row should be mark zero
# because of the overlapping of the top left cell
# iterating the matrix except the first row and column
# iterate the first column
# iterate the first row

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    
                    for row in range(len(matrix)):
                        if matrix[row][j] != 0:
                            matrix[row][j] = float('inf')
                    
                    for col in range(len(matrix[i])):
                        if matrix[i][col] != 0:
                            matrix[i][col] = float('inf')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
        
        return


    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    else:
                        matrix[i][0] = 0
                    
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0



