from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0 
        ans = 0
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == '1': 
                    ans += 1
                    q = deque([(i, j)])
                    self.markIsland(grid, q, m, n)
        return ans
    
    def markIsland(self, grid, q, rows, cols): 
        """
        Precondition: queue holds a tuple of the form (row, col), or is empty
        """
        while q: 
            row, col = q.popleft()
            if row < 0 or row == rows or col < 0 or col == cols: 
                pass
            elif grid[row][col] == '1': 
                grid[row][col] = '#'
                q.append((row + 1, col))
                q.append((row, col + 1))
                q.append((row - 1, col))
                q.append((row, col - 1))

def main():
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    sol = Solution()
    assert sol.numIslands(grid) == 1

if __name__ == "__main__":
    main()