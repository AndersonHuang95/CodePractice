class Solution:
    def exist(self, board, word):
        """
        This is a graph search problem, we can solve it either recursively or iteratively.

        In this particular problem, we may have to use DFS from every valid spot...
        
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0]) if board else 0 
        for row in range(rows):
        	for col in range(cols): 
        		if self.backtrack(board, word, row, col, 0): return True
        return False

    def backtrack(self, board, word, row, col, idx): 
    	# --- base cases ---
    	if idx == len(word): return True
    	if row < 0 or col < 0 or row == len(board) or col == len(board[0]): return False 

    	# --- try every direction: up, down, left, right ---
    	if board[row][col] != word[idx]: return False 

    	tmp, board[row][col] = board[row][col], '.'
    	ans = self.backtrack(board, word, row + 1, col, idx + 1) \
    		or self.backtrack(board, word, row, col + 1, idx + 1) \
    		or self.backtrack(board, word, row - 1, col, idx + 1) \
    		or self.backtrack(board, word, row, col - 1, idx + 1)
    	board[row][col] = tmp
    	return ans 


        