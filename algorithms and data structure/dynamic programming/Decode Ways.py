# https://leetcode.com/problems/decode-ways/description/

# brute force approach
# The time complexity is O(2^n). 
# In each iteration there is 2 subproblem, and the height of the tree is len(s)

def numDecodings(s: str) -> int:
    res = [0]
    hash_set = {str(i) for i in range(1,27)}

    def dfs(s, start, end):
        if end == len(s) and s[start:end] in hash_set:
            res[0] += 1
            return
        
        if end > len(s) or s[start:end] not in hash_set:
            return
        
        dfs(s, end, end+1)
        dfs(s, end, end+2)
    
    dfs(s, 0, 1)
    dfs(s, 0, 2)

    return res[0]

# the base case is a single character string
# if adding one character to the current char is also valid, 
# add the cached value to the current result
def numDecodings(s: str) -> int:
    dp = [0 for i in range(len(s)+1)]
    dp[-1] = 1

    hash_set = {str(i) for i in range(1,27)}

    for i in range(len(s)-1,-1,-1):
        if s[i] in hash_set:
            dp[i] = dp[i+1]
        
        if i+2 <= len(s) and s[i:i+2] in hash_set:
            dp[i] += dp[i+2]
    
    return dp[0]