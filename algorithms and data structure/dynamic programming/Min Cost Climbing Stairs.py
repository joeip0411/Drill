# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List


# the cost of going to the destination from the current node is the cost of the current node plus the minimum of next 2 nodes, we only need to keep track of the cost of the next 2 nodes
# Time complexity is O(n) and space complexity is O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost)

        dp = [cost[-2], cost[-1]]

        for i in range(len(cost)-3,-1,-1):
            temp = min(dp[1], dp[0]) + cost[i]
            dp[1] = dp[0]
            dp[0] = temp
        
        return min(dp[0], dp[1])


        