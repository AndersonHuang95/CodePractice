#!/usr/bin/env python3

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

import math

class Solution:
    def evalRPN(self, tokens):
        """Evalutes a list representing Revese Polish Notation

        Reverse Polish Notation is a fancy way of saying postfix notation. Assuming we
        don't have ot worry about parentheses, we can simply use a stack to 
        keep track of our operands, and since we are guaranteed a valid RPN, we
        pop two items when we need to perform a calculation

        :type tokens: List[str]
        :rtype: int
        """

        def is_integer(s): 
            """Determines if a string is a valid integer
            """
            if not s: return False
            i = 1 if s[0] == '-' or s[0] == '+' else 0
            while i < len(s): 
                if not s[i].isdigit(): return False
                i += 1
            return True

        operands = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                try: 
                    op2 = operands.pop()
                    op1 = operands.pop()
                except IndexError as e: 
                    print(e, "Invalid Reverse Polish Notation")
                expression = op1 + token + op2
                result = eval(expression)
                # --- make sure we floor for positive results, and ceil 
                # for negative results (we want to round towards 0)
                result = math.floor(result) if result > 0 else math.ceil(result)
                operands.append(str(result))
            elif is_integer(token):
                operands.append(token)
            else: 
                raise ValueError("Invalid token in Reverse Polish Notation")
        ans = int(operands.pop())
        return ans
                
def main(): 
    x = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    sol = Solution()
    print(sol.evalRPN(x))

if __name__ == '__main__':
    main()