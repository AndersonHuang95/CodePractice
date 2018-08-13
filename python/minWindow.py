import collections

class Solution:
	def minWindow(self, s, t):
		if not s or not t: return ""
		
		# --- count how many chars we need to search for ---
	    needs, missing = collections.Counter(t), len(t)

	    # --- initialize vars for current range and min range ---
	    begin = min_begin = min_end = 0

	    # --- search for chars in larger string --- 
	    for end, c in enumerate(s, 0):
	        missing -= (needs[c] > 0)
	        needs[c] -= 1
	        # --- attempt to shrink the window if no more chars are missing ---
	        if not missing:
	            while begin < end and needs[s[begin]] < 0:
	                needs[s[begin]] += 1
	                begin += 1
	            if not min_end or end - begin <= min_end - min_begin:
	                min_begin, min_end = begin, end
	    return s[min_begin:min_end + 1]

sol = Solution()
print(sol.minWindow("frefdom", "fdom"))