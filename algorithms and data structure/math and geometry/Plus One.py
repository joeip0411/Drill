# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []

        for i in range(len(digits)-1, -1, -1):
            d = digits[i] + 1 + carry if i == len(digits) - 1 else digits[i] + carry

            if d >= 10:
                carry = 1
                d -= 10
            else:
                carry = 0

            res.append(d)
        
        if carry > 0:
            res.append(carry)
        
        return res[::-1]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = 0
        digits = digits[::-1]

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            
            i += 1
        
        return digits[::-1]