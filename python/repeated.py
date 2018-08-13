class Solution:
    def repeatedStringMatch(self, A, B):
        """
        Determine if A is in B.
        If A is in B, then a substring match is possible.
        should be ceil(len(B) / len(A))
        
        special cases: 
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        if not m: 
            return -1
        if not B: 
            return 1
        mult = 1
        while len(A) < 2 * len(B): 
            A += A
            mult += 1
            if B in A: 
                return mult
        return -1

def main():
    a = "abcd"
    b = "cdabcdab"
    sol = Solution()
    print(sol.repeatedStringMatch(a, b))

if __name__ == "__main__":
    main()