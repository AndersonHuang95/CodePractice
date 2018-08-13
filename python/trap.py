class Solution:
    def trap(self, height):
        """
        For each position, if non-zero, find the nearest column with height
        greater than or equal, start there after


        Assumes valid height array, so no negatives 

        if no column with greater than or equal height, proceed to next index
        :type height: List[int]
        :rtype: int
        """

        # two pointer method
        ans = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while (left < right): 
        	if height[left] > height[right]:
        		if height[left] > max_left: max_left = height[left]
        		else: ans += (max_left - height[left])
        		left += 1
        	else:
        		if height[right] > max_right: max_right = height[right]
        		else: ans += (max_right - height[right])
        		right -= 1
        return ans

sol = Solution()
print(sol.trap([0,7,1,4,6]))


