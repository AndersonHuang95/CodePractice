class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.strip()
        seen_exponent = False
        seen_decimal = False
        for char in s: 
        	if char.isalpha() and char != 'e': return False
        	elif char == 'e' and seen_exponent: return False
        	elif char == 'e': seen_exponent = True; seen_decimal = False
        	elif char == '.' and seen_decimal: return False
        	elif char == '.': seen_decimal = True
        	elif not char.isdigit(): return False
        return True

sol = Solution()
print(sol.isNumber("0"))
print(sol.isNumber("0.1"))
print(sol.isNumber("abc"))
print(sol.isNumber("1 a"))
print(sol.isNumber("2e10"))