from typing import List


# Time complexity O(mn) to build the prefix matrix
# Space complexity O(mn)
# Time complexity for sumRegion is O(1)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            cur_sum = 0
            for j in range(len(matrix[i])):
                cur_sum += matrix[i][j]
                self.prefix[i][j] = cur_sum

                if i > 0:
                    self.prefix[i][j] += self.prefix[i-1][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole = self.prefix[row2][col2]

        top = self.prefix[row1 - 1][col2] if row1 - 1 >= 0 else 0

        left = self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        
        top_left = self.prefix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        
        res = whole - top - left + top_left

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)# param_1 = obj.sumRegion(row1,col1,row2,col2)# param_1 = obj.sumRegion(row1,col1,row2,col2)# param_1 = obj.sumRegion(row1,col1,row2,col2)