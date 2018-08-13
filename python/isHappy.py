class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = set()
        ans = n 
        while ans != 1:
            digits, x = [], 0
            while ans: 
                digit = ans % 10
                x += digit**2
                digits.append(digit)
                ans //= 10
            tup = tuple(digits)
            ans = x
            if tup in table: 
                return False 
            else: 
                table.add(tup)
        return True

def main():
    sol = Solution()
    assert sol.isHappy(19) == True
    assert sol.isHappy(235135123512351325) == False

if __name__ == '__main__':
    main()
