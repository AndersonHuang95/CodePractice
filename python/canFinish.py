class GraphNode:
    def __init__(self, value=None, neighbors=None):
        self.value = value if value else 0 
        self.neighbors = neighbors if neighbors else set()
    
    def addNeighbor(self, neighbor): 
        self.neighbors.add(neighbor)
    
    def getNeighbors(self):
        return self.neighbors
    
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        This is a topological sort problem. There may be two ways to solve this problem
        1. Look for a cycle -> cycle detection
        2. Topological sort the problem 
        
        Be wary of mutable default arguments.

        Let V denote number of courses, E denote the number of edges

        Such an algorithm is O(E) in runtime and O(E) in space.
        
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        

        # --- Create adjacency list representation: O(E) ---
        adj_list = [GraphNode() for _ in range(numCourses)]
        for pair in prerequisites: 
            adj_list[pair[0]].addNeighbor(pair[1])    

        # --- Determine how many edges enter every node O(E) ---
        in_edges = [0 for _ in range(numCourses)]
        for node in adj_list: 
            for neighbor in node.getNeighbors(): 
                in_edges[neighbor] += 1
        
        # --- Find nodes with in_edges of 0, these are the nodes we can start at (no requirements): O(V) ---
        candidates = []
        for i in range(numCourses):
            if in_edges[i] == 0: 
                candidates.append(i)
        
        # --- Try to take all courses, when we successfully take one, modify in_edges accordingly: O(E) ---
        topological_ordering = []
        while candidates: 
            current = candidates.pop()
            topological_ordering.append(current)
            for neighbor in adj_list[current].getNeighbors(): 
                in_edges[neighbor] -= 1
                if in_edges[neighbor] == 0: 
                    candidates.append(neighbor)
        
        return len(topological_ordering) == numCourses

def main():
    sol = Solution()
    e1 = [[1,0],[0,1]]
    assert sol.canFinish(2, e1) == False

    e2 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    assert sol.canFinish(6, e2) == True

if __name__ == '__main__':
    main()
        
        