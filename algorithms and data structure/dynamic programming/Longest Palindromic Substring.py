# https://leetcode.com/problems/longest-palindromic-substring/description/

# from a chosen character, expand outward to see whether the new substring is a palindrome
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_length = 0

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        res = s[left:right+1]
                else:
                    break
                left -= 1
                right += 1
            
            left = i
            right = i+1

            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        res = s[left:right+1]
                else:
                    break

                left -= 1
                right += 1

        return res