# https://leetcode.com/problems/daily-temperatures/

from typing import List


# start from the end
# array to store the smallest pos of a tempereature seen so far
# for each position in the temperature array, scan the cache and find the smallest position with a greater temperature
# Time complexity is O(71n) -> O(n)
# Space complexity is O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_arr = [float('inf') for i in range(30, 101)]
        res = [0 for _ in range(len(temperatures))]

        offset = 30
        temp_arr[temperatures[-1] - offset] = len(temperatures) - 1

        for i in range(len(temperatures)-2,-1,-1):
            temp_arr[temperatures[i]-offset] = i

            pos = float('inf')
            for j in range(temperatures[i] - offset + 1, 101 - offset):
                pos = min(pos, temp_arr[j])
            
            if pos != float('inf'):
                res[i] = pos - i
        
        return res
    

# Compare current item to the top of the stack, if cur item is greater,
# pop from stack and add difference in position ot result, keep popping until cur item is <= last item of stack or stack is empty
# add the current item to the stack
# Time complexity is O(n)
# Space complexirt is O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = [(0, temperatures[0])]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = i - item[0]
            
            stack.append((i, temperatures[i]))
        
        return res


