class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Invariant: nums1 is guarnteed to have enough space to hold the initialized elements,
        (m + n) of them, in nums1 and num2s combined.

        We simply go through both lists and add the element that is the lesser of the two
        at each current index in both arrays. To not risk having to shift elements, 
        we fill from the back. 

        Example: 

		1 2 4 x x x
			^
		3 5 6 
			^

		1 2 4 x x 6 
			^
		3 5 6
		  ^

		1 2 4 x 5 6
		    ^
		3 5 6 
		^

		1 2 4 4 5 6
		  ^
		3 5 6
		^ 

		1 2 3 4 5 6
		  ^
		3 5 6 
	   ^

	   	1 2 3 4 5 6
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        current = m + n - 1
        while i >= 0 and j >= 0:
        	if nums1[i] >= nums2[j]: 
        		nums1[current] = nums1[i]
        		i -= 1
        	else: 
        		nums1[current] = nums2[j]
        		j -= 1
        	current -= 1

        if i >= 0: 
        	while i >= 0: 
        		nums1[current] = nums1[i]
        		i -= 1
        		current -= 1

        if j >= 0:
        	while j >= 0:
        		nums1[current] = nums2[j]
        		j -= 1
        		current -= 1

        return nums1
