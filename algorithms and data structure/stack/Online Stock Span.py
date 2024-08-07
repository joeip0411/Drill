# https://leetcode.com/problems/online-stock-span/

# a number can never access value that is to the left of a value that is greater than itself.
# Use a stack to compress the stock span together
# Time complexity = O(n)
# Space complexity = O(n)

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1

        while self.stack and self.stack[-1][0] <= price:
            item = self.stack.pop()
            count += item[1]
        
        self.stack.append((price, count))

        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)