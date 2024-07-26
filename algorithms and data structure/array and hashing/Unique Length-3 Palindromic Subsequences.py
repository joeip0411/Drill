# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

# a triple nested for loop will be O(n^3)

class Solution:
    # first and last character must be the same
    # the number of unique character in the window
    # Time complexity = O(n^2)
    # Space complexity = O(n)
    def countPalindromicSubsequence(self, s: str) -> int:
        
        res = 0
        hash_map = {}

        for i, val in enumerate(s):
            if val not in hash_map:
                hash_map[val] = [i, i]
            else:
                hash_map[val][1] = i
        
        for start, end in hash_map.values():
            counter = set()

            for i in range(start+1, end):
                counter.add(s[i])
            res += len(counter)
        
        return res
    

    # Time complexity = O(26n)
    def countPalindromicSubsequence(self, s: str) -> int:
        
        hash_map = {}
        res = set()

        # O(n)
        for i, val in enumerate(s):
            if val not in hash_map:
                hash_map[val] = [i, i]
            else:
                hash_map[val][1] = i
        
        # O(n)
        for i in range(1, len(s) - 1):
            # O(1)
            for v in hash_map.values():
                if v[0] < i < v[1]:
                    palindrome = (s[v[0]], s[i])
                    res.add(palindrome)
        
        return len(res)