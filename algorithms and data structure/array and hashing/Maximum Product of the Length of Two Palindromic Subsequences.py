# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/

# Bit masking to find all possible subsequence and detecting conflicting subsequence.
# Brute Force approach
class Solution:

    def maxProduct(self, s: str) -> int:

        hash_map = {}
        N = len(s) - 1
        res = 0

        for i in range(1, 1 << N+1):
            subseq = ''
            for j in range(N+1):
                if (i & 1 << j):
                    subseq += s[len(s) - j - 1]
            
            if subseq == subseq[::-1]:
                hash_map[i] = len(subseq)

        for k1 in hash_map:
            for k2 in hash_map:
                if k1 & k2 == 0:
                    res = max(res,hash_map[k1] * hash_map[k2])
        
        return res