# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
        
        return res
    

sorted([[3,2],[1,2]], )
'k' * 3 + 'd'*2