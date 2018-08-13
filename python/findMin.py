#!/usr/bin/env python3 

class Solution:
    def findMin(self, nums):
        """Finds minimum element in a rotated, sorted array 
        
        This is a variant of the binary search. Instead of finding a direct match, we are finding
        the direct minimum, which is similar. The algorithm can be broken down into several parts. 
        We still have the notion of a start and ending index, but the ending index in this case must
        lie within the array, since we will be using it to decide which part of the array to continue
        our search. The algorithm is as follows. 
        
        1. Check if a[s] < a[e]. 
            a. Yes? -> a[s] is the minimum in our range, so return it
            b. No? -> goto 2
        2. Calculate m = s + (e - s) // 2, AKA middle of range. Check if a[s] <= a[m]
            a. Yes? -> since a[s] > a[e] but a[s] <= a[m], the minimum will lie in the second half
            recurse on range (m + 1, e)
            b. No? -> since a[s] > a[e] and a[s] > a[m], the minimum will lie in the first half
            recurse on range (b, m)
            
        Args: 
            nums (List[int]) - input array
        
        Returns: 
            int - minimum in array 
        """
        start, end = 0, len(nums) - 1
        while start < end: 
            if nums[start] < nums[end]: 
                return nums[start] 
            mid = start + (end - start) // 2
            if nums[mid] == nums[end]: 
                end -= 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]

sol = Solution()
print(sol.findMin([10, 1, 10, 10, 10]))