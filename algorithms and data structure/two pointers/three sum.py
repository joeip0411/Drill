from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            # to make sure we never use the same item as the first element twice
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # to make sure we never use the same combination of the first and second item twice
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue

                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
            
            