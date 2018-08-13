class Solution:
    def solve(self, board):
        """
        Example:

        X X X X
        X O O X
        X X O X
        X O X X

        Output:

        X X X X
        X X X X
        X X X X
        X O X X

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # --- go through board, ignore borders --- 
        m, n = len(board), len(board[0]) if board else 0
        for i in range(1, m - 1): 
            for j in range(1, n - 1): 
                if board[i][j] == 'O': 
                    

        