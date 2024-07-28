from typing import List


# Sort the array, so that item with similar values are closest to each other.
# Then build array of size 3, and compare front and end to see if the difference is <= k
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        temp = []
        res = []

        for n in nums:
            if len(temp) == 3:
                if temp[-1] - temp[0] <= k:
                    res.append(temp)
                    temp = []
                else:
                    return []

            temp.append(n)
        
        if temp[-1] - temp[0] <= k:
            res.append(temp)
        else:
            return []
        
        return res
    
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                temp = nums[i: i+3]
                res.append(temp)
            
        return res
