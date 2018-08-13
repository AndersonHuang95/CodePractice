class Solution:
    def permute(self, nums):
        """
        This is a classic backtracking problem. Let's try an example.

        1 2 3 
		^
		s   for a valid index in (s, len(nums)): swap with s, backtrack with s = index + 1, reverse swap 

			1 2 3
			  ^
			  s 	for a valid index in (s, len(nums)): swap with index 2 (no-op), backtrack with s = index + 1, reverse swap 

				1 2 3
					^
					s 	... swap with index 3 (no-op) ... 

					1 2 3
						  ^		
						  s  s > len(nums): bottom out; add to return array 
			1 3 2
			  ^
			  s 	swap with elt @ index 2: backtrack with s = index + 1, reverse swap

				1 3 2 ... swap with index 3 (no-op) ... 
					^ 
					s

					1 3 2
						  ^ 
						  s s > len(nums): bottom out; add to return array 

		2 1 3 valid index is at idx = 1, swap with s, backtrack with s = index + 1, reverse swap 
		^		
		s 	

			2 1 3
			  ^ 
			  s

				2 1 3
				    ^ 
				    s

					2 1 3
					      ^ 
					      s s > len(nums): bottom out; add to return array 

		... and so on ... 

		3 2 1

		... 	... 

					3 2 1
					      ^ 
					      s s > len(nums): bottom out; add to return array 

		Let's say you start with 1 2 3; Because we want to return a list of all permutations, 
		we need a return array and a candidate array; the candidate array can just be the 
		original nums array. But we need a variable so we can observe a base case for the recursion
		to bottom out. 

		Now let's put this algorithm into words 
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        self.backtrack(nums, ret, 0)
        return ret

    def backtrack(self, nums, ret, start): 
    	# Base case: bottom out
    	# Take care to append a deep copy
        if start == len(nums):
            ret.append(nums[:])
            return

        if start > 0: 
            while start < len(nums) and nums[start] == nums[start - 1]: start += 1

        for idx in range(start, len(nums)): 
            nums[start], nums[idx] = nums[idx], nums[start]
            self.backtrack(nums, ret, start + 1)
            nums[start], nums[idx] = nums[idx], nums[start] 


    def iterative_permute(self, nums): 
        perms = [[]]
        for num in nums: 
            nxt = []
            for perm in perms: 
                # the number of positions for a permuation is len(permutation) + 1
                # e.g. 
                #  1 2 3 (permutation)
                # ^ ^ ^ ^ there are 4 positions to insert 
                for idx in range(len(perm) + 1): 
                    nxt.append(perm[:idx] + [num] + perm[idx:])
                    if idx < len(perm) and perm[idx] == num: break 
            perms = nxt
        return perms

sol = Solution()
perm = sol.permute([1, 1, 2, 1])
print(perm)


