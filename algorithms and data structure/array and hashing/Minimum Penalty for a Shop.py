# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# An ordinary prefix and postfix sum question
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_prefix = [1 if char == 'N' else 0 for char in customers] 
        y_postfix = [1 if char == 'Y' else 0 for char in customers]

        for i in range(1, len(n_prefix)):
            n_prefix[i] += n_prefix[i-1]
        
        for i in range(len(y_postfix)-2, -1, -1):
            y_postfix[i] += y_postfix[i+1]

        min_penalty = float('inf')
        pos = -1

        for i in range(len(n_prefix)):
            n_penalty = n_prefix[i-1] if i > 0 else 0
            y_penalty = y_postfix[i]
            total_penalty = n_penalty + y_penalty

            if total_penalty < min_penalty:
                min_penalty = total_penalty
                pos = i
        
        if n_prefix[-1] < min_penalty:
            pos = len(n_prefix)

        return pos