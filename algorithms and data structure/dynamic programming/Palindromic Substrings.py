# https://leetcode.com/problems/palindromic-substrings/

# start from a certain character and expand outward
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            left = right = i
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    res += 1
                else:
                    break
                left -= 1
                right += 1

            left = i
            right = i+1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    res += 1
                else:
                    break
                left -= 1
                right += 1

        return res
