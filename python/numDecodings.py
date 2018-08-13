class Solution:
    def numDecodings(self, s):
        """
        'A' -> 1
		'B' -> 2
		...
		'Z' -> 26

        Input: "226"
		Output: 3
		Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

		This is a chunking problem. Since each letter can be encoded as up to 2 digits, we need
		to chunk the string into either 1 or 2 digit chunks. This seems like a good choice 
		for recursion, since we build our answer from subproblems. For the "226" example...

		2 2 6
	   ^		ps = (s[:1] + ps[1:]) or (s[:2] + ps[2:])

	   		2 2 6 	"B" + 
			  ^

				2 2 6 	"B" + 
					^ 

					2 2 6 	"F" -> add to list
						  ^ 
						  
					2 2 6		-> out of range, discard 
							^

				2 2 6 		"Z"	-> add to list
					  ^

	   		2 2 6 	"V"
	   			^

	   			2 2 6 	"F" -> add to list
					  ^
	   			2 2 6     -> out of range, discard
	   				    ^
	   	But god damn it this is a DP problem. 

        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n: return 0

        table = [0 for _ in range(n + 1)]

        # --- start from the front ---
        table[n] = 1
        table[n - 1] = 1 if s[n - 1] != '0' else 0

        for i in range(n - 2, -1, -1): 
        	if s[i] == '0': continue
        	table[i] = table[i + 1] + table[i + 2] if int(s[i:i + 2]) < 27 else table[i + 1]
        return table[0]

sol = Solution()
print(sol.numDecodings("27"))


