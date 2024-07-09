# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

# cumulative product of prefix X cumulative product of postfix

def productExceptSelf(nums: List[int]) -> List[int]:

    prefix = 1
    postfix = 1
    res = [prefix]

    
    for i in range(len(nums)-1): # O(n)
        prefix *= nums[i]
        res.append(prefix)

    for j in range(len(nums)-1, 0, -1): # O(n)
        postfix *= nums[j]
        res[j-1] = res[j-1] * postfix
    
    return res