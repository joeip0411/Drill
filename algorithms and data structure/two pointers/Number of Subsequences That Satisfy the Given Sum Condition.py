
# the order of the item does not matter, because the total number of subsequence is the same e.g. 1,2 vs 2,1, target = 3, results are the same
# brute force is O(2^n), aim for something better

# O(n^2)
from typing import List


def numSubseq(nums: List[int], target: int) -> int:


    nums.sort()
    mod = 10 ** 9 + 7

    res = 0
    i = 0

    while i < len(nums) and nums[i] <= target:
        power = -1
        j = i

        while j < len(nums) and nums[i] + nums[j] <= target:
            power += 1
            j += 1

        res += 2 ** power if power > -1 else 0
        res = res % mod

        i += 1

    return res

# sort than binary search
# Time complexity = O(n log n)
def numSubseq(nums: List[int], target: int) -> int:

    nums.sort()
    
    mod = 10 ** 9 + 7
    res = 0
    i = 0

    while i < len(nums) and nums[i] <= target:

        left = i
        right = len(nums) - 1
        power = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[i] + nums[mid] <= target:
                power = mid - i
                left = mid + 1
            else:
                right = mid - 1

        res += 2 ** power if power > -1 else 0
        res = res % mod

        i += 1

    return res