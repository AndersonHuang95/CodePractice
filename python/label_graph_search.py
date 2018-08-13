#!/usr/bin/env python3

from collections import defaultdict

class Node:
    def __init__(self, label):
        self.label = label

class Solution:
    def __init__(self):
        self.nodes = [Node(0)]
        self.graph = defaultdict(list)

    def preprocess(self, labels, edges):
        for label in labels:
            self.nodes.append(Node(label))

        # edges must be even length
        if len(edges) % 2 == 1: 
            raise ValueError("Edges list is an invalid format")
        idx = 0
        while idx < len(edges):
            self.graph[edges[idx]] += [edges[idx + 1]]
            self.graph[edges[idx + 1]] += [edges[idx]]
            idx += 2

    def longest_labeled_path(self, labels, edges):
        self.preprocess(labels, edges)
        longest = [0]
        for start in range(1, len(self.nodes) + 1):
            self.dfs(start, longest, set(), 1)
        return longest[0]

    def dfs(self, start, longest, seen, current):
        # compensate for 0-indexing for nodes
        seen.add(start)
        longest[0] = max(longest[0], current)
        for neighbor in self.graph[start]:
            print(start, neighbor)
            if neighbor not in seen and self.nodes[start].label == self.nodes[neighbor].label:
                self.dfs(neighbor, longest, seen, current + 1)

def main():
    A = [1, 1, 1, 2, 2, 1]
    E = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6]
    sol = Solution()
    print(sol.longest_labeled_path(A, E))

if __name__ == "__main__":
    main()


