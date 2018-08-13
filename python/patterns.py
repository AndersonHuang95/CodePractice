class Solution:
    def numberOfPatterns(self, m, n):
        """
        Solve using BFS and DFS
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

        neighbors = {
            1: {2, 4, 5},
            2: {1, 3, 4, 5, 6},
            3: {2, 5, 6},
            4: {1, 2, 5, 7, 8},
            5: {1, 2, 3, 4, 6, 7, 8, 9},
            6: {2, 3, 5, 8, 9},
            7: {4, 5, 8},
            8: {4, 5, 6, 7, 9},
            9: {5, 6, 8}
        }

        ans = [0]
        current = set()
        valid = set()
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                self.dfs(matrix, neighbors, valid, m, n, row, col, current, ans)
        return ans[0]

    def dfs(self, matrix, neighbors, valid, m, n, row, col, current, ans):
        if row < 0 or row == 3 or col < 0 or col == 3:
            return

        digit = matrix[row][col]
        current.add(digit)
        if len(current) >= m and len(current) <= n:
            ans[0] += 1
        if len(current) > n:
            return
        for num in set(range(1, 10)) - current:
            if num not in current and (num in neighbors[digit] or num in valid):
                valid |= (neighbors[digit] & neighbors[num])
                self.dfs(matrix, neighbors, valid, m, n, num // 3, num % 3, current, ans)

def main():


if __name__ == '__main__':
    main()


        