from typing import List


class Solution:
    # face up -> min power
    # face down -> max power
    # Time complexity = O(n log n)
    # Space complexity = O(1)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        res = 0
        cur = 0
        
        up = 0
        down = len(tokens)

        while up < down:
            if power >= tokens[up]:
                cur += 1
                res = max(res, cur)
                power -= tokens[up]
                up += 1
            else:
                if cur > 0:
                    cur -= 1
                    down -= 1
                    power += tokens[down]
                else:
                    return res
        
        return res