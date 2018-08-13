#!/usr/bin/env python3

class Solution:
    def longestIncreasingPath(self, matrix):
        """Naive DFS will take us O(m^2 * n^2)
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        if m == 0 or n == 0:
            return 0
        ans = 0
        table = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                ans = max(ans, self.dfs(matrix, m, n, row, col, table))
        return ans

    def dfs(self, matrix, rows, cols, row, col, table):
        if table[row][col] == 0:
            longest_neighboring_path = 0
            for x, y in ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)):
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[row][col]:
                    longest_neighboring_path = max(longest_neighboring_path, self.dfs(matrix, rows, cols, x, y, table))
            table[row][col] = 1 + longest_neighboring_path
        return table[row][col]
        # for x, y in ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)):
        #     if 0 <= x < rows and 0 <= y < cols:
        #         if matrix[x][y] > matrix[row][col] and not seen[x][y]:
        #             seen[x][y] = True
        #             if table[x][y] == 1:
        #                 self.dfs(matrix, rows, cols, x, y, current + 1, longest, seen, table)
        #             else:
        #                 longest[0] = max(longest[0], current + table[x][y])
        #             seen[x][y] = False
        # longest[0] = max(longest[0], current)

def main():
    a = [
          [9,9,4],
          [6,6,8],
          [2,1,0]
        ] 

    b = [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ] 

    sol = Solution()
    print(sol.longestIncreasingPath(a))
    print(sol.longestIncreasingPath(b))

if __name__ == '__main__':
    main()