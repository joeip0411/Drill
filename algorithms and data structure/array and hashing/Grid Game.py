# https://leetcode.com/problems/grid-game/

from typing import List


# There are n path for the red robot to choose
# first row calculate prefix sum
# second row calculate postfix sum
def gridGame(grid: List[List[int]]) -> int:

    prefix_sum = []
    postfix_sum = []

    points = 0

    for i in range(len(grid[0])):
        points += grid[0][i]
        prefix_sum.append(points)
    
    points = 0
    for j in range(len(grid[1])-1, -1, -1):
        points += grid[1][j]
        postfix_sum.append(points)
    postfix_sum = postfix_sum[::-1]
    max_idx = 0
    max_points = 0

    print(prefix_sum)
    print(postfix_sum)
    for i in range(len(prefix_sum)):
        total_points = prefix_sum[i] + postfix_sum[i]
        if total_points > max_points:
            max_points = total_points
            max_idx = i
    
    print(max_idx)
    upper_points = sum([grid[0][i] for i in range(max_idx+1, len(grid[0]))])
    lower_points = sum([grid[1][j] for j in range(max_idx - 1, -1, -1)])

    res = max(upper_points, lower_points)
    return res


gridGame([[20,3,20,17,2,12,15,17,4,15],
          [20,10,13,14,15,5,2,3,14,3]])
