from typing import List


# This is a prefix sum problem
# Find the most common prefix sum across all the row except the last prefix sum
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash_map = {}
        total_length = sum(wall[0])

        for i in range(len(wall)):
            prefix_sum = 0

            for j in range(len(wall[i])):
                prefix_sum += wall[i][j]
                if prefix_sum != total_length:
                    hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1

        freq_map = {v:k for k, v in hash_map.items()}

        for i in range(len(wall), 0, -1):
            if i in freq_map:
                return len(wall) - i
        
        return len(wall)
