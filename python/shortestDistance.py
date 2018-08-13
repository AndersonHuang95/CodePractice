from collections import deque

class Solution:
    def shortestDistance(self, grid):
        """
        Let's optimize by starting from the 1's instead of the 0's
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        distances = [[0] * n for _ in range(m)]
        reachable_buildings = [[0] * n for _ in range(m)]
        num_ones = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    num_ones += 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    self.BFS(grid, m, n, row, col, distances, reachable_buildings)

        ans = float("inf")
        for row in range(m):
            for col in range(n):
                if reachable_buildings[row][col] == num_ones:
                    ans = min(ans, distances[row][col])
        return ans if ans != float("inf") else -1
    
    def BFS(self, grid, rows, cols, row, col, dist, rb):
        """Performs BFS
        """
        q = deque({(row, col, 0)})
        seen = [[False for _ in range(cols)] for _ in range(rows)]
        while q: 
            i, j, dist = q.popleft()
            if i < 0 or i == rows or j < 0 or j == cols:
                continue
            seen[i][j] = True
            if grid[i][j] == 0:
                dist[i][j] += dist
                rb[i][j] += 1
            q.append((i - 1, j, dist + 1))
            q.append((i, j + 1, dist + 1))
            q.append((i + 1, j, dist + 1))
            q.append((i, j - 1, dist + 1))
            
def main():
    grid = [[1, 0, 2, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]]
    sol = Solution()
    print(sol.shortestDistance(grid))

if __name__ == '__main__':
    main()
            
        