from typing import List


class Solution:
    # left = max(weights)
    # right = sum(weights)
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def possible(weights, days, max_capacity):
            cur_capacity = max_capacity
            day_count = 1

            for w in weights:
                if cur_capacity < w:
                    day_count += 1
                    if day_count > days:
                        return False
                    cur_capacity = max_capacity
                cur_capacity -= w

            return True

        res = 0
        left = 0
        right = 0

        for w in weights:
            left = max(left, w)
            right += w
        
        while left <= right:
            mid = (right + left) // 2

            if possible(weights, days, mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res