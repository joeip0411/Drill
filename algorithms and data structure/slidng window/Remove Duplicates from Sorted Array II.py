from typing import List


# Time complexity O(n^2)
# Space complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        end = len(nums)

        while r < end:
            # keep finding different item
            if nums[l] == nums[r]:
                r += 1
                continue
            # item occurs <= 2 times , no shifting
            if r - l <= 2:
                l = r
            # more than 2 times, shift the whole array to the left
            else:
                cur = l + 2

                for i in range(r, end):
                    nums[cur] = nums[i]
                    cur += 1
                # shift end to left
                end -= r - (l+2)
                # start from next proper item
                l = l + 2
                r = l

        # edge case, last occurs more than 2 times
        if end - l >= 2:
            end -= r - (l + 2)       
        
        return end 

# Time complexity O(n)
# Space complexity O(1)

# Find the last occurence of an item, replace left position by item for at most 2 times
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        
        while r < len(nums):
            count = 1

            while r + 1 < len(nums) and nums[r + 1] == nums[r] :
                r += 1
                count += 1
            
            for i in range(min(2,count)):
                nums[l] = nums[r]
                l += 1
            
            r += 1
        
        return l
