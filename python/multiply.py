#!/usr/bin/env python3

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        ans, factor = 0, 1
        for digit1 in num1[::-1]: 
        	tmp, inner_factor = 0, 1
        	for digit2 in num2[::-1]: 
        		tmp += (inner_factor * int(digit1) * int(digit2))
        		inner_factor *= 10
        	ans += (tmp * factor)
        	factor *= 10
        return str(ans)

sol = Solution()
print(sol.multiply("25", "25"))