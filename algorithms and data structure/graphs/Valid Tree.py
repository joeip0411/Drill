from typing import List


class Solution:
    # A tree here means all the nodes are connected, and there cannot be any cycles

    # property 1: number of edges = number of nodes - 1
    # property 2: the distinct count of nodes in edges list = number of nodes
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # edge case of one node tree
        if len(edges) == 0 and n == 1:
            return True

        hash_set = set()

        for node1, node2 in edges:
            hash_set.add(node1)
            hash_set.add(node2)
        
        return len(hash_set) == n and len(edges) == n-1
    
    # Using DFS, since we are using a adjacency list, which contains both the parent and child
    # It doesn not matter which node we start with
    # We pick node 0 because it always exists
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = { i: [] for i in range(n) }

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()

        def dfs(i, prev):

            # cycle
            if i in visited:
                return False
            
            visited.add(i)

            for neighbour in adj[i]:
                if neighbour == prev:
                    continue
                    
                no_cycle = dfs(neighbour, i)
                if not no_cycle:
                    return False
            
            return True
        
        no_cycle = dfs(0,-1)

        return no_cycle and len(visited) == n
        
s = set()
s.add(1)
s.remove(1)