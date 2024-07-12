from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()
        pacific = set()
        atlantic = set()
        res = []

        def dfs(i,j, prev_height, start):
            # out of bounds
            if (i,j) in visited\
            or min(i,j) < 0\
            or i >= len(heights)\
            or j >= len(heights[0]):
                return
            # higher land
            if prev_height < heights[i][j]:
                return
            # next to ocean
            if i == 0 or j == 0:
                pacific.add(start)
            if i == len(heights) -1 or j == len(heights[i]) - 1:
                atlantic.add(start)
            
            visited.add((i,j))

            up = dfs(i-1, j, heights[i][j], start)
            down = dfs(i+1, j, heights[i][j], start)
            left = dfs(i, j-1, heights[i][j], start)
            right = dfs(i, j+1, heights[i][j], start)

            visited.remove((i,j))
        
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                dfs(i,j, float('inf'), (i,j))
        
        for coordinate in pacific:
            if coordinate in atlantic:
                res.append(list(coordinate))
        
        return res

# moving from ocean to inland with DFS, no backtracking
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []

        def dfs(i,j, prev_height, ocean):
            # out of bounds
            if (i,j) in ocean\
            or min(i,j) < 0\
            or i >= len(heights)\
            or j >= len(heights[0]):
                return
            # moving from low to high
            if prev_height > heights[i][j]:
                return
            
            ocean.add((i,j))

            dfs(i-1, j, heights[i][j], ocean)
            dfs(i+1, j, heights[i][j], ocean)
            dfs(i, j-1, heights[i][j], ocean)
            dfs(i, j+1, heights[i][j], ocean)
        

        for j in range(len(heights[0])):
            dfs(0,j,-1,pacific)
            dfs(len(heights)-1,j,-1,atlantic)
        
        for i in range(len(heights)):
            dfs(i,0,-1,pacific)
            dfs(i,len(heights[0])-1,-1,atlantic)
        
        for coordinate in pacific:
            if coordinate in atlantic:
                res.append(list(coordinate))
        
        return res


