# https://leetcode.com/problems/word-break/

# start from the end, an empty string can always be matched
# move forward by 1 char and see whether a word can be match, 
# if true, that means if we start from position i, we can math the whole word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        
        return dp[0]