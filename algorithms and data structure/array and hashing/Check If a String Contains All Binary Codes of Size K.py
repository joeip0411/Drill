# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    # hash all string of length k
    # count of all binary string of length k = 2^k

    # Time complexity = O(n)
    # Space complexity = O(n)
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash_set = set()

        for i in range(len(s) - k + 1):
            hash_set.add(s[i:i+k])
        
        return len(hash_set) == 2**k
        