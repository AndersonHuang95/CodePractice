class Solution:
    def combine(self, n, k):
        """
        Example:

        Input: n = 4, k = 2
		Output:
		[
		  [2,4],
		  [3,4],
		  [2,3],
		  [1,2],
		  [1,3],
		  [1,4],
		]

		We seek to produce all combinations of 1...n given n. Recalling combinatorics, the 
		formula for the number of combinations given the collection and the size of the 
		desired combination is

		n choose k = n! / k! (n - k)! 

		For the example above, the number of combinations = 4! / (2! * 2!) = 6

		This problem is different from the permutations and subsets variations. Let's think through
		how we would solve this problem.

		1 2 3 4
		^ ^ 
		p p 

		[1, 2] 		found combo

		1 2 3 4
		^	^
		p 	p 		

		[1, 3]		found combo 

		1 2 3 4		
		^	  ^
		p 	  p 	

		[1, 4] 		found combo, end of iter

		1 2 3 4
		  ^	^
		  p p

		[2, 3]		found combo

		1 2 3 4
		  ^	  ^
		  p   p

		[2, 4]		found combo, end of iter

		1 2 3 4
		    ^ ^
		    p p 

		[3, 4]		found combo, end of iter, end of choices 

		Working through an example, it seems that we begin with the first index, and continue choosing until we have
		no more choices for k. We can write both an iterative and a recursive program to do this job. Let's do both.
		We ensure that we don't repeat any combinations by never going back in the array. That is, each time a number
		is the starting candidate, we try to add (k - 1) more numbers to form a valid combo, but these numbers
		always come in a forward fashion. We will not look back in the array. 

        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        cand, ans = [], []
        self.backtrack(1, n, k, cand, ans)
        return ans 

    def backtrack(self, current, n, k, cand, ans): 
    	if len(cand) == k: 
    		ans.append(cand[:])
    		return
    	for num in range(current, n + 1): 
    		cand.append(num)
    		self.backtrack(num + 1, n, k, cand, ans)
    		cand.pop()

sol = Solution()
print(sol.combine(4, 2))


        