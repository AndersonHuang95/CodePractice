from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums):
        if not nums: return 0 
        table = {}
        idx, longest = 0, 0
        while idx < len(nums): 
            n = nums[idx]
            if n not in table: 
                left = table[n - 1] if (n - 1) in table else 0
                right = table[n + 1] if (n + 1) in table else 0
                print(n, left, right)
                ans = left + right + 1
                table[n] = ans
                longest = max(longest, ans)
                table[n - left] = ans
                table[n + right] = ans
            idx += 1
            # --- duplicates ---
        return longest

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
        