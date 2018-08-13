#!/usr/bin/env python3

from collections import deque

class Solution:
    def minTotalDistance(self, grid):
        """Finds minimum distance to all homes in a grid

        Idea is to use BFS to start a search from every '0' cell
        We'll need a visited array. 
        We'll return the minimum of all these results.
        This first attempt at a solution is O(m^2 * n^2)
        where m and n are the dimensions of grid.

        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0]) if grid else 0
        if rows == 0 or cols == 0:
            raise ValueError("Invalid grid supplied")

        ans = float("inf")
        for row in range(rows):
            for col in range(cols):
                ans = min(ans, self.bfs(grid, rows, cols, row, col, set()))
        return ans

    def bfs(self, grid, rows, cols, row, col, visited):
        frontier = deque()
        frontier.append((row, col))
        dist = 0
        while frontier:
            nrow, ncol = frontier.popleft()
            if (nrow, ncol) in visited:
                continue
            if grid[nrow][ncol] == 1:
                dist += self.manhattanDistance(nrow, ncol, row, col)
            for i, j in [(nrow - 1, ncol), (nrow, ncol + 1), (nrow + 1, ncol), (nrow, ncol - 1)]:
                if (i, j) not in visited and i >= 0 and i < rows and j >= 0 and j < cols:
                    frontier.append((i, j))
            visited.add((nrow, ncol))
        return dist

    def manhattanDistance(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

def main():
    grid = [[0,0,0,0,1,0,1,0],
            [0,0,0,0,1,0,0,1]]
    sol = Solution()
    print(sol.minTotalDistance(grid))

if __name__ == '__main__':
    main()
