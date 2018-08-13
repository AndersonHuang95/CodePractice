class Solution:
    def searchMatrix(self, matrix, target):
        """
        Example:

        Input:
		matrix = [
		  [1,   3,  5,  7],
		  [10, 11, 16, 20],
		  [23, 30, 34, 50]
		]
		target = 13
		Output: false

		Let's treat the entire 2D Matrix as a sorted list. This will simplify our assumptions
		We can just do binary search, and the expected runtime is O(log(m + n))

		How do we do this? 
		The left bound is 0 and the right bound is (m * n - 1) 

		Like any binary search, we halve the search space by doing 

		mid = (left + right) // 2

		However, we must do a conversion step to get back 2D coordinates, since we will be 
		working as if the 2D matrix is in 1D form. The key is this conversion 

		Let's say we are looking at the number 11 in the 2D array above. Since its in position 
		... 5 and in the 1st row and in the 1st column (0-indexing), we will somehow need to 
		get formulas for this conversion.

		One way to derive the formula is to go from 2D to 1D first. To get the 1D coordinate, we just do
		(row_num) * size_of_col + col_num. For our example... 

		(1 * 4) + 1 = 5 

		Doing this in the reverse manner, 

		The row number is simply the 1D representation divided by the number of cols, then floored. 
		The column number is the number mod the number of cols. 

        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m, n = len(matrix), len(matrix[0]) if matrix else 0
        begin, end = 0, m * n 

        while begin < end: 
        	mid = (begin + end) // 2
        	row = mid // n 
        	col = mid % n 
        	print(row, col)
        	if matrix[row][col] == target: return True
        	elif matrix[row][col] < target: begin = mid + 1
        	else: end = mid  
        return False
        