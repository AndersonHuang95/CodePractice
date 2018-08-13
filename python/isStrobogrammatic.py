class Solution:
    def isStrobogrammatic(self, num):
        """
        The only numbers that appear the same turned upside down:

        0 -> 0
        1 -> 1
        6 -> 9
        8 -> 8
        9 -> 6

        2 -> 7 and 7 -> 2 is a bit of a stretch, so I will not include it.
        
        The cases with 1 and 8 are simple. We just need to be wary of the 6's and
        9's.

        For example, obviously 111 is strobogrammatic.
        Unfortunately, 619 is less obvious. Rotating 180 degrees still yields 619.

        A solution similar to palindromic integer could solve this, but will use O(n)
        space. There may not be a way around this since we must keep a copy if we wish
        to do operations on the original number while checking the new number.

        We might also have to worry about 0's.

        :type num: str
        :rtype: bool
        """

        def is_mirrored(a, b):
            """
            Args:
                a (int): a should be within 0 - 9
                b (int): b should be within 0 - 9
            Returns:
                bool:
            """
            return (a in {0, 1, 8} and a == b) or (a == 6 and b == 9) or (a == 9 and b == 6)

        rev, other = 0, int(num)
        while other: 
            rev = rev * 10 + other % 10
            other //= 10

        num = int(num)
        while num and rev:
            first = num % 10 
            second = rev % 10
            if not is_mirrored(first, second):
                return False
            num //= 10
            rev //= 10
        return not num and not rev

def main():
    sol = Solution()
    assert sol.isStrobogrammatic(0) == True
    assert sol.isStrobogrammatic(609) == True
    assert sol.isStrobogrammatic(555) == False
    assert sol.isStrobogrammatic(655) == False
    assert sol.isStrobogrammatic(1060901) == True
    assert sol.isStrobogrammatic(67) == False
    assert sol.isStrobogrammatic(1000) == False

if __name__ == "__main__":
    main()


        