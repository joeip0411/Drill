# https://leetcode.com/problems/rotate-image/

from typing import List


# each layer requires end - start - 1 iteration
# each iteration will rotate exactly 4 grids
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix) - 1

        while start <= end:
            for i in range(end-start):
                temp = matrix[end][start+i]
                matrix[end][start+i] = matrix[end-i][end]
                matrix[end-i][end] = matrix[start][end-i]
                matrix[start][end-i] = matrix[start+i][start]
                matrix[start+i][start] = temp
            start += 1
            end -= 1