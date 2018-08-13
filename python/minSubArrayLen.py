#/usr/bin/env python3

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Can you code an O(n) solution and an O(n log n) solution?

# Dicussion:
# This is a problem concerned with subarrays. Subarrays by definition are continuous and
# are fixed by a starting point and an endpoint. In a subarray of length n, we have n choose
# 2 ways of fixing these two points. This results in O(n^2) subarrays. To check each one, 
# we have to use O(n) time in the worst case. This naive solution is O(n^3) which isn't very good.

# Like with many array problems, we can cleverly use two pointers to arrive at an optimal solution.
# The cleverness lies in the bookkeeping. Let our variables be left, right, total, and minLength.

# left: left pointer (starts at 0)
# right: right pointer (also starts at 0) 
# total: running total of subarray within left/right
# minLength: tracks the minimum length of the subarray that satisfies our conditions, if applicable

# We start with total being the first element. We constantly check if we are over or at our target.
# We can exit early if our first element meets the conditions, since we can't possibly beat a minimum
# length of 1. If we are under, we slide the right pointer. If we are over we slide the left pointer.

# We notice that we only use up O(n) time since left and right take on the entire array of values in 
# [0, n) once and only once. 

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            raise ValueError("Array cannot be empty")

        left, right = 0, 0
        minLength = float("inf")
        total = nums[left]

        while right < len(nums) and left <= right:
            if total < s:
                right += 1
                current = 0 if right == len(nums) else nums[right]
                total += current
            else: 
                minLength = min(right - left + 1, minLength)
                total -= nums[left] 
                left += 1
        return minLength

def main():
    a = [2, 3, 1, 2, 4, 3]
    b = [2, 2, 2, 10, 10, 2, 2, 25, 0, 0]
    sol = Solution()
    print(sol.minSubArrayLen(7, a))
    print(sol.minSubArrayLen(27, b))

if __name__ == '__main__':
    main()

