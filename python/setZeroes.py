class Solution:
    def setZeroes(self, matrix):
        """
        Example: 

        Input: 
		[
		  [0,1,2,0],
		  [3,4,5,2],
		  [1,3,1,5]
		]
		Output: 
		[
		  [0,0,0,0],
		  [0,4,5,0],
		  [0,3,1,0]
		]

		A first attempt at a solution would be to have row and column marker lists. A first pass
		over the matrix would take note of all rows and columns that a 0 is in. Then a second pass 
		would go thru and mark all those columns and rows as zeroed out. This is a O(m + n) space solution, 
		but can we do better, and utilize constant space? 

		We should notice that there should be no way to do a single-pass solution. If we mark 0's in a first-pass
		solution, we lose track of which 0's were in the original array, thus foiling our attempt.

		To iterate to an optimal and correct solution, we must do some in-place caching of the rows and columns
		that we need to change. After some verification, we see that the extra lists for the to-be-changed
		rows and columns are altogether unnecessary! The only detail that needs extra attention is the 
		first row/first column. Simply marking (0, 0) is ambigious, so we must take care to have
		two flags that tell us if we need to clear out the first row or column. The algorithm that follows
		is O(n) time and O(1) space. We do not confuse our 0's because we are always marking cells that 
		we have already seen.

        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        ### Find rows and cols to clear ###
        clear_first_row = clear_first_col = False
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0 
        for i in range(rows): 
        	for j in range(cols): 
        		if matrix[i][j] == 0:
        			if i == 0: 
        				clear_first_row = True
        			if j == 0: 
        				clear_first_col = True
        			matrix[i][0], matrix[0][j] = 0, 0

        ### Clear rows 
        for i in range(1, rows): 
        	if matrix[i][0] == 0: 
        		for j in range(1, cols): 
        			matrix[i][j] = 0

        ### Clear columns 
        for j in range(1, cols): 
        	if matrix[0][j] == 0: 
        		for i in range(1, rows): 
        			matrix[i][j] = 0

        ### Check first row and first column ###
        if clear_first_col: 
        	for i in range(rows): 
        		matrix[i][0] = 0

        if clear_first_row: 
        	for j in range(cols): 
        		matrix[0][j] = 0


