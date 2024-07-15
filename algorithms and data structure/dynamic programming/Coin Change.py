# https://leetcode.com/problems/coin-change/description/
from typing import List



def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf') for i in range(amount + 1)]
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
            dp[i] = min(1 + dp[i-coin], dp[i])
        
    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1

coinChange([2], 4)