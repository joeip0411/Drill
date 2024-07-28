# https://leetcode.com/problems/sequential-digits/

from typing import List


# 2 digits: base 1, increment 11
# 3 digits: base 12, increment 111
# 4 digits: base 123, incrment 1111
# 5 digits: base 1234, increment 11111
def sequentialDigits(low: int, high: int) -> List[int]:
    res = []

    base = 1
    power = 1
    increment = base + 10 ** power

    while True:
        num = base + increment

        while num % 10 != 0:
            if num <= high:
                if num >= low:
                    res.append(num)
                num += increment
            else:
                return res

        base += increment
        power += 1
        increment += 10 ** power

from collections import deque


# Using a queue
# 78 -> 789 is 78 * 10 + 9, but this does not apply to 89, this will be become 890 + 10 = 900
def sequentialDigits(self, low: int, high: int) -> List[int]:
    q = deque(range(1, 10))
    res = []

    while q:
        num = q.popleft()

        if num > high:
            continue
        if low <= num <= high:
            res.append(num)

        digit = num % 10
        
        if digit < 9:
            new_num = num * 10 + (digit + 1)
            q.append(new_num)
    
    return res

