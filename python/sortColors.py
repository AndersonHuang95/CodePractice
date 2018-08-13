class Solution:
    def sortColors(self, nums):
        """
        We are given that a two-pass solution is trivial, so we will try to find 
        the optimal one-pass solution.

        Example:

        [2, 1, 0, 1, 2, 0]
		->
		[0, 0, 1, 1, 2, 2]

		The two-pass algorithm keeps track of three counts, one for each color.
		At the end, we rewrite the array according to the counts. The question is now, 
		how can we make the first pass obsolete. In effect, we will need to factor
		in the counting and overwriting during the same pass. Some ideas that come
		to mind are boundaries. If there were only two colors, we could use 
		two pointers to implement the solution, much like a sliding window. 

		Let's try if a three-pointer solution will work.

		2	1	0	1	2	0
		^	^				^
		i 	j 				k swap 2 and 0

		0	1	0	1	2	2

		^	^			^	
		i 	j 			k	

		... 

		Each time we examine a number in the array, and at most we are doing constant work.

		This is O(n) and a one-pass soluton now.
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1

        while j <= k: 
        	if nums[j] == 0: 
        		nums[i], nums[j] = nums[j], nums[i]
        		i += 1
        		j += 1
        	elif nums[j] == 1: 
        		j += 1
        	else: 
        		nums[j], nums[k] = nums[k], nums[j]
        		k -= 1

sol = Solution()
x = [2, 0, 1, 0, 0, 0, 1, 1, 1, 2, 2, 1, 2, 0, 0]
sol.sortColors(x)
print(x)