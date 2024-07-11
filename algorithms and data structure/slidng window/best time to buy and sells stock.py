from typing import List

# we don't want to buy a stock at a price which is higher than previously seen
# we can keep track of the lowest price seen so far, this is the purchase price
# in each iteration, calculate the difference between current price and lowest price seen so far

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_purchase_price = float('inf')

        for price in prices:
            lowest_purchase_price = min(lowest_purchase_price, price)
            profit = price - lowest_purchase_price
            max_profit = max(profit, max_profit)
        
        return max_profit