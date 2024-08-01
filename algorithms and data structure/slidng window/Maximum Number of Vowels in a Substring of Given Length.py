# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Classic sliding window problem, nothing special
# Time complexity = O(n)
# Space complexity = O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(k):
            if s[i] in vowels:
                count += 1
            res = max(res, count)
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            res = max(res, count)
        
        return res
    
# A cleaner solution
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            
            if i - left + 1 > k:
                count -= 1 if s[left] in vowels else 0
                left += 1
            
            res = max(res, count)
        
        return res
            