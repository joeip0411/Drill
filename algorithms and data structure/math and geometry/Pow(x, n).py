# https://leetcode.com/problems/powx-n/description/

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        temp = x

        for i in range(abs(n) - 1):
            temp = temp * x
        
        if n > 0:
            return temp
        else:
            return 1/temp
        

# Time complexity: O(log n)
# Space compelxity: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:

        cache = {
            0: 1,
            1: x,
        }

        def pow_recur(x, n):
            if n in (0,1):
                return cache[n]
            
            if n not in cache:
                temp = pow_recur(x, n // 2)
                cache[n] = temp * temp * (x if n % 2 == 1 else 1)
            return cache[n]
        
        res = pow_recur(x, abs(n))

        return res if n > 0 else 1 / res
                