# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

# two pointers to fast forward repeated characters
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            while left + 1 < len(s) and s[left + 1] == s[left]:
                left += 1
            
            while right > left and right - 1 > 0 and s[right - 1] == s[right]:
                right -= 1

            right -= 1
            left += 1

        res = 0 if right < left else right - left + 1

        return res

# cleaner solution
# store numbers to compare in temporary variable
# compare left and right to temp
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            temp = s[left]

            while left <= right and s[left] == temp:
                left += 1
            while left <= right and s[right] == temp:
                right -= 1
        
        return right - left + 1