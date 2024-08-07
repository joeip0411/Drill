# https://leetcode.com/problems/simplify-path/

# ignore '.', pop from stack if '..', otherwise keep appending
# add '/' to the original path to make sure the last item is append to the stack
# Time complexity = O(n)
# Space complexity = O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'
        
        cur = []
        res = []

        for char in path:
            if char == '/':
                if not cur:
                    continue
                else:
                    cur_dir = ''.join(cur)

                    if cur_dir not in ('..', '.'):
                        res.append(cur_dir)
                    elif cur_dir == '..' and res:
                        res.pop()

                    cur = []
            else:
                cur.append(char)
        
        
        return '/' + '/'.join(res)