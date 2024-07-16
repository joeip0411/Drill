# https://neetcode.io/problems/count-connected-components

from typing import List


class Solution:
    # build adjacency list
    # build a set to store all nodes in the graph
    # visited set to avoid traversing the same node twice
    # pop a node from the node set and do a dfs, count the number of popping
    # needs to account for nodes not connected to anything

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n)}
        nodes = set()
        visited = set()
        res = 0

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

            nodes.add(node1)
            nodes.add(node2)
        
        def dfs(i, prev):
            nonlocal n

            if i in visited:
                return
            
            visited.add(i)
            nodes.remove(i)
            n -= 1

            for neighbour in adj[i]:
                if neighbour == prev:
                    continue
                dfs(neighbour, i)

        while nodes:
            for node in nodes:
                break
            dfs(node, -1)
            res += 1
        
        return res + n
