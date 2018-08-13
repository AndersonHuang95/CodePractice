from copy import deepcopy
from collections import deque

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        seen = {}
        ans = self.dfs(node, seen)
        return ans
    
    def dfs(self, node, seen):
        if not node: return node

        if node in seen: return seen[node]
        ans = UndirectedGraphNode(node.label)
        seen[node] = ans
        for neighbor in node.neighbors: 
            ans.neighbors.append(self.dfs(neighbor, seen))
        return ans

    def print_graph(self, node, seen): 
        if not node: return
        print("Node :", node.label)
        print("\tneighbors", node.neighbors)
        seen[node] = True
        for neighbor in node.neighbors: 
            if neighbor not in seen: 
                self.print_graph(neighbor, seen)


g0 = UndirectedGraphNode(0)
g1 = UndirectedGraphNode(1)
g2 = UndirectedGraphNode(2)
g0.neighbors = [g1, g2]
g1.neighbors = [g0, g2]
g2.neighbors = [g0, g1, g2]

sol = Solution()
g = sol.cloneGraph(g0)
sol.print_graph(g, {})

