# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])

        return res