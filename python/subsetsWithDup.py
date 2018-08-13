class Solution:
    def subsetsWithDup(self, nums):
        """
        Let's think back to our original subset problem, without duplicates. 

        For a set such as [1, 2, 3], this is how we would start

        [] - empty set is always there 
        [] [1] - add 1 to all existing sets
        [] [1] [2] [1 2]	- add 2 to all existing sets
        [] [1] [2] [1 2] [3] [1 3] [2 3] [1 2 3] 	- add 3 to all existing sets

        out of numbers to add. We are done.

        Now, what happens when we try this on a set with duplicates? 

        [1, 2, 2]

        [] 
        [] [1]
        [] [1] [2] [1 2]
		[] [1] [2] [1 2] [2] [1 2] [2 2] [1 2 2]

		We get two duplicate sets: [2] and [1, 2]. But we still get unique subsets such as [2 2]
		and [1 2 2] by adding the second 2. This means our new rule can't simply ignore duplicate
		numbers. What is the trick? 

		Perhaps we have to ignore the first-half of the elements when we add. This is the way we would
		proceed given that the nums array is already sorted. If the array were not sorted, we would
		have to go through the current subsets in answer, and the ones that do not already have the
		duplicate number in the set, we would not add to. 

		For example, in the above set: [1, 2, 2], we would not add to [] or [1] because the num 2 was 
		already added from a previous iteration. To prevent having to cycle through the entire array 
		each time, we simply begin my sorting the array. 


        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]
        nums.sort()
        unique_added = 0
        for i, num in enumerate(nums): 
        	start, next_subsets = 0, []
        	if i > 0 and nums[i - 1] == num: start = len(ans) - unique_added
        	for subset in ans[start:]: 
        		next_subsets.append(subset + [num])
        	unique_added = len(next_subsets)
        	ans += next_subsets
        return ans

sol = Solution()
print(sol.subsetsWithDup([2, 2]))
print(sol.subsetsWithDup([1, 2, 2]))
print(sol.subsetsWithDup([1, 2, 2, 2]))
