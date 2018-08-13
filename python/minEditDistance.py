class Solution:
    def minDistance(self, word1, word2):
        """
        This is a classic dynamic programming problem. Let's first try framing it as a recursion problem.

        Say we have two strings: 'apple' and 'orange'

        How would we attempt to retrieve the minimum edit distance? 
        Naively, we could just go from right to left and try to match up characters. 

        apple
			^
        orange
        	 ^

       	match

       	apple 
		   ^
       	orange
			^

		mismatch, change letter 
		... 
		apple 
		^
		orange
		^

		And so on, until we get a total of 5 edits (1 insert, 4 replacements) 

		Naively, it seems we can define the solution at index n as a formula of its subproblems...

		dp[i][j] = dp[i - 1][j - 1] 			   if a[i] == b[j] (characters match)
		dp[i][j] = min(1 + dp[i - 1][j - 1],	   if a[i] != b[j] (mismatch, should we delete or replace?)
				   1 + min(dp[i - 1][j], dp[i][j - 1]))	
		
		The second part of the recurrence relation is complicated since we can either replace the letter completely, 
		which means we add 1 plus whatever the minimum was for the match for the previous indexes on both characters.

		The delete is also involved. We add 1, but revert to the minimum edit distance of either matching i's previous 
		index with our current index, or matching j's previous index with i's current index. 

		This is the rough sketch of a dynamic programming solution. Below we see the table is filled in, with 
		r = replacement
		d = delete 
		i = insert 
			
			''	o 	r 	a 	n 	g 	e
		''	0 	1i	2i	3i	4i	5i	6i
	
		a 	1i  1r  2r	3r	4r	5r	6r

		p 	2i 	

		p 	3i

		l 	4i

		e 	5i

        :type word1: str
        :type word2: str
        :rtype: int
        """

        len1, len2 = len(word1), len(word2)
        table = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        ### base constraints ###
        for i in range(len1 + 1): 
        	table[i][0] = i
        for i in range(len2 + 1): 
        	table[0][i] = i

        ### dynamic programming ###

        for i in range(1, len1 + 1): 
        	for j in range(1, len2 + 1): 
        		if word1[i - 1] == word2[j - 1]: 
        			table[i][j] = table[i - 1][j - 1]
        		else: 
        			table[i][j] = min(1 + table[i - 1][j - 1],
        								1 + min(table[i - 1][j], table[i][j - 1]))
        return table[-1][-1]

sol = Solution()
print(sol.minDistance('apple', 'orange'))