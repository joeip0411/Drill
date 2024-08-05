# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

# concat the original string to itself
# point wise comparison to the two target
# Time complexity = O(n)
# Space complexity = O(n)
class Solution:
    def minFlips(self, s: str) -> int:
        
        s = s + s
        target1 = ['0' if i % 2 == 0 else '1' for i in range(len(s))]
        target2 = ['1' if i % 2 == 0 else '0' for i in range(len(s))]

        def min_flip_extended(s, target):

            left = 0
            res = float('inf')
            diff = 0
            length = len(s)//2

            for right in range(len(s)):
                if s[right] != target[right]:
                    diff += 1

                if right - left + 1 > length:
                    if s[left] != target[left]:
                        diff -= 1
                    left += 1
                
                if right - left + 1 == length:
                    res = min(diff, res)
            
            return res
        
        r1 = min_flip_extended(s, target1)
        r2 = min_flip_extended(s, target2)

        return min(r1, r2)





