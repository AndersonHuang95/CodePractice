class Solution:
    def subsets(self, nums):
        """

        Example: 

        Input: nums = [1,2,3]
		Output:
		[
		  [3],
		  [1],
		  [2],
		  [1,2,3],
		  [1,3],
		  [2,3],
		  [1,2],
		  []
		]
        :type nums: List[int]
        :rtype: List[List[int]]

        We can view the problem of forming subsets as successively adding items to a list. Let's clarify. 

        For a given n, there are 2^n subsets. Each element has two choices, it can be in a set or not 
        in a set. Let's do a simple example. 

        1 2 3 

        [] start with empty

        [] [1] 	add 1 to all sets in current candidate

        [] [1] [2] [1 2]	add 2 to all sets in current candidate

        [] [1] [2] [1 2] [3] [1 3] [2 3] [1 2 3] add 3 to all sets in current candidate

        out of nums to add. Done!

     	The iterative solution is a little more straightforward.

     	Recursively...


        """

        ans = [[]]
        for num in nums: 
        	nxt = ans[:]
        	for subset in ans: 
        		tmp = subset[:]
        		tmp.append(num)
        		nxt.append(tmp)
        	ans = nxt
        return ans

sol = Solution()
print(sol.subsets([1, 2, 3]))